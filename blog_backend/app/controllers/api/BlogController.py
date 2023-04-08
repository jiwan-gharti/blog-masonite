from masonite.controllers import Controller
from masonite.views import View
from app.models.Blog import Blog
from masonite.request import Request
from masonite.filesystem import Storage
from masonite.authentication import Auth
from masonite.response import Response
from masonite.validation import Validator


class BlogController(Controller):
    
    def index(self, request: Request,auth: Auth):
        user_ = request.user()
        print(user_)
        if user_:
            if user_.is_admin:
                return Blog.all()
            return Blog.get_user_related_blogs(user=user_).get()
        return {"error":"no loggedIn"}


    def show(self, view: View):   
        # return Blog.find(self.request.param('id'))
        try:
            if blog := Blog.find(self.request.param('id')):
                return blog
            return {"error":"Blog not found."}
        except Exception as e:
            return {"error":"Blog not found."}

    def store(self, request: Request, storage: Storage):
        path = storage.disk('local').put_file('blogs', request.input('image'))
        data = {
            'title':request.input('title'),
            'content':request.input('content'),
            'image':path,
            'user_id':request.user().id,
        }
        object = Blog.create(**data)
        return object

    def update(self, request:Request,storage: Storage):
        blog_id = request.param("id")
        try:
            object = Blog.where("id",blog_id).first()
            if object and object.user_id == request.user().id:
                data = request.all()
                updated_data = object.update(data)
                return updated_data
            else:
                return {'error':"permission denied"}
        except Exception as e:
            print(e)
            return {"error": "not updated."}

    def destroy(self, request: Request):
        user_ = request.user()
        try:
            object = Blog.where("id", self.request.param('id')).first()
            if not object:
                return {"error":"Blog not found"}

            if object and (object.user_id == user_.id or user_.is_admin):
                _ = object.delete()
                return {"response":"successfully deleted"}
            else:
                return {'error':"Permission denied."}
        except Exception as e:
            return {"error":"Blog not deleted"}

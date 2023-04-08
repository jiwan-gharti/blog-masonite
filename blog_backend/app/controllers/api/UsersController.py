from masonite.controllers import Controller
from masonite.views import View
from app.models.User import User
from masonite.request import Request

class UsersController(Controller):
    def __init__(self, request:Request, view: View) -> None:
        self.request = request
        self.view = view

    def index(self, request: Request):
        user = request.user()
        if user and user.is_admin:
            return User.all()
        return {'error':"Permission denied. Need super admin privillage"}

    def show(self, view: View):
        try:
            user = User.find(self.request.param('id'))
            if not user:
                return {'error':"user not found"}
            if user.id == self.request.user().id or self.request.user().is_admin:
                return user
            else:
                return {"error":"Permission denied! Need super admin privillage"}
        except Exception as e:
            return {"error":"User not found."}

    def store(self, view: View):
        data = {
            'name':self.request.input('name'),
            'email':self.request.input('email'),
            'password':self.request.input('password'),
            'second_password':self.request.input('second_password'),
            'phone':self.request.input('phone'),
            'content':self.request.input('content'),
            'is_admin':self.request.input('is_admin'),
        }
        object = User.create(**data)
        return object

    def update(self, request: Request):
        user = request.user()
        user_id = request.param('id')
        try:
            if not user:
                return {'error':"not found"}

            if user and (user_id == user.id or user.is_admin):
                data = request.all()
                updated_user = user.update(data)
                return updated_user
            else:
                return {'error':"permission denied"}
        except Exception as e:
            return {"error": "not updated."}

    def destroy(self, request: Request):
        try:
            user = User.where('id',self.request.param('id')).first()
            if not user:
                return {'error':"not found"}
            if user and user.id == request.user().id and request.user().is_admin:
                _ = user.delete()
                return {'success':"Deleted Successfully"}
            else:
                return {"error":"permission denied"}
        except Exception as e:
            return {'error':"no deleted"}


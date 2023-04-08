""" Blog Model """

from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masoniteorm.relationships import belongs_to




class Blog(Model):
    """Blog Model"""

    __table__ = 'blogs'
    __with__ = 'users'

    @belongs_to('user_id', 'id')
    def users(self):
        from app.models.User import User
        return User
    
    @staticmethod
    def get_user_related_blogs(user):
        return Blog.where('user_id',user.id)
    
    @staticmethod
    def get_all_blogs():
        return Blog.all()


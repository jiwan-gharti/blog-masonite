"""User Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masonite.authentication import Authenticates
from masonite.api.authentication import AuthenticatesTokens


# class User(Model, SoftDeletesMixin, Authenticates):
class User(Model,AuthenticatesTokens,SoftDeletesMixin, Authenticates):
    """User Model."""


    __table__ = 'users'
    __fillable__ = ["name", "email", "password","is_admin"]
    __hidden__ = ["password","api_token","second_password"]
    __auth__ = "email"
    __primary_key__ = 'id'

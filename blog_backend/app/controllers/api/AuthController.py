from masonite.request import Request
from masonite.response import Response
from masonite.controllers import Controller
from app.models.User import User
from masonite.authentication import Auth

import jwt
from masonite.environment import env

class AuthController(Controller):
    def logout(self, request: Request, response: Response, auth: Auth):
        auth = auth.logout()
        return response.json({'message': 'Successfully logged out'})
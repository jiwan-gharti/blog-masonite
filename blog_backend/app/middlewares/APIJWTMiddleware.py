from masonite.request import Request
from masonite.response import Response
from masonite.middleware import Middleware
from app.models.User import User
# from masonite.exceptions import UnauthorizedException
import jwt

class APIAuthenticationMiddleware(Middleware):

    def __init__(self, request: Request):
        super().__init__(request)

    @staticmethod
    def decode_token(token, secret_key):
        try:
            decoded = jwt.decode(token, secret_key, algorithms=['HS256'])
            return decoded
        except jwt.ExpiredSignatureError:
            # Handle expired token
            raise Exception('Token expired. Please log in again.')
        except jwt.InvalidTokenError:
            # Handle invalid token
            raise Exception('Invalid token. Please log in again.')


    def before(self):
        bearer_token = self.request.header('Authorization')
        if bearer_token:
            try:
                token = bearer_token.split()[1]
                print("----------------------------middleware--------")
                print(token)
                decoded_token = AuthenticationMiddleware.decode_token(token) # decode the token
                user = User.where('id', decoded_token.get('sub')).first()
                if user:
                    self.request.set_user(user) # add the authenticated user to the request object
                else:
                    raise 
            except:
                raise 
        else:
            raise 

from masonite.routes import Route
from masonite.api import Api

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    # Route.post('api/auth',"AuthenticationController@auth"),

]
ROUTES += Api.routes(auth_route="/api/auth", reauth_route="/api/reauth")
# routes/api.py
from masonite.routes import Route

ROUTES = [
    Route.post('logout', "api.AuthController@logout"),

    Route.api('users', "api.UsersController"),
    Route.api('blogs', "api.BlogController")
]


from litestar import Litestar

from src.routes import ROUTES

app = Litestar(route_handlers=ROUTES)

from aiohttp import web

from timer_data.api.routes import create_routes
from timer_data.db import Base
from timer_data.db_connectivity import engine
from timer_data.middlewares import login_middleware, error_middleware


def create_app() -> web.Application:
    app = web.Application(
        middlewares=[
            login_middleware,
            error_middleware
        ]
    )
    app.add_routes(create_routes())
    return app


if __name__ == '__main__':
    Base.metadata.create_all(engine())
    web.run_app(create_app())

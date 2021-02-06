from aiohttp import web
from functools import wraps


def login_required(f):
    @wraps(f)
    async def wrapper(request):
        if request['user'] is None:
            return web.json_response({'message': 'Unauthorized'}, status=401)
        return await f(request)
    return wrapper

from aiohttp import web
from jwt import DecodeError
from timer_data.api.utils import decode_token


@web.middleware
async def login_middleware(request, handler):
    cookies = request.cookies
    user_data = None
    try:
        user_data = decode_token(cookies.get('token', ''))
    except DecodeError:
        pass
    finally:
        request['user'] = user_data
    return await handler(request)


@web.middleware
async def error_middleware(request, handler):
    try:
        return await handler(request)
    except Exception as e:  # TODO: refactor in the future
        print(e)
        return web.json_response({'error': str(e)}, status=403)

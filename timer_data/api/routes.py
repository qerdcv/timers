from aiohttp import web
from timer_data.api import api


def create_routes():
    return [
        web.get('/api/ping', api.ping),
        web.post('/api/register', api.create_user),
        web.post('/api/login', api.login),
        web.get('/api/logout', api.logout),
        web.post('/api/timer', api.create_timer),
        web.get('/api/user/{user_id}/timers', api.get_timers),
        web.get('/api/user/{user_id}/timer/{id}', api.get_timer)
    ]

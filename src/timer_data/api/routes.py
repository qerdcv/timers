from aiohttp import web
from timer_data.api import api


def create_routes():
    return [
        web.get('/api/ping', api.ping),
        web.post('/api/register', api.create_user),
        web.post('/api/login', api.login),
        web.get('/api/logout', api.logout),
        # timer
        web.post('/api/timer', api.create_timer),
        web.get('/api/timers', api.get_all_timers),
        web.patch('/api/timer/{id}/stop', api.stop_timer),
        # user
        web.get('/api/user/{user_id}/timers', api.get_timers),
        web.get('/api/user/{user_id}/timer/{id}', api.get_timer)
    ]

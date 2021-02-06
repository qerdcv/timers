from datetime import datetime
from aiohttp import web

from timer_data.api.utils import encode_user_password, encode_token, dump_timer
from timer_data.db import User, Timer
from timer_data.db_connectivity import session
from timer_data.decorators import login_required


async def index():
    return web.json_response({'message': 'ok'})


async def ping(request):
    return web.json_response({'message': 'pong'})


async def create_user(request):
    data = await request.json()
    user = User(**data)
    user.password = encode_user_password(user.password)
    with session() as s:
        s.add(user)
        s.commit()
    return web.json_response({'id': user.id}, status=201)


async def login(request):
    data = await request.json()
    with session() as s:
        user = s.query(User).filter_by(username=data['username']).first()
    if not user:
        return web.json_response(
            {'message': f'User with username {data["username"]} not found'},
            status=404,
        )
    if encode_user_password(data['password']) != user.password:
        return web.json_response(
            {'message': 'Wrong password'},
            status=403,
        )
    resp = web.HTTPFound('/')
    resp.set_cookie('token', encode_token(user), max_age=86400, httponly=True)
    return resp


async def logout(request):
    resp = web.HTTPFound('/')
    resp.set_cookie('token', '', max_age=0)
    return resp


@login_required
async def create_timer(request):
    data = await request.json()
    data['user_id'] = request['user']['id']
    timer = Timer(**data)
    with session() as s:
        s.add(timer)
        s.commit()
    return web.json_response({'id': timer.id})


async def get_timers(request):
    with session() as s:
        timers = s.query(Timer)
        if not request['user'] or request['user']['id'] != int(request.match_info['user_id']):
            return web.json_response(
                timers
                .filter_by(user_id=int(request.match_info['user_id']), is_private=False).all(),
                dumps=dump_timer
            )
        return web.json_response(
            timers
            .filter_by(user_id=int(request.match_info['user_id'])).all(),
            dumps=dump_timer
        )


async def get_timer(request: web.Request):
    with session() as s:
        timer = s.query(Timer).filter(
                Timer.user_id == int(request.match_info['user_id']), Timer.id == int(request.match_info['id']),
            ).first()
    if (not request['user'] or request['user']['id'] != int(request.match_info['user_id'])) and timer.is_private:
        return web.json_response({'message': 'Not found'}, status=404)
    return web.json_response(timer, dumps=dump_timer)


@login_required
async def stop_timer(request: web.Request):
    with session() as s:
        timer = s.query(Timer).filter_by(user_id=request['user']['id']).first()
        timer.is_stopped = True
        timer.to_date = datetime.utcnow()

        s.commit()
    return web.json_response({'message': 'ok'})

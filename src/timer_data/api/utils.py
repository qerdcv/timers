import hashlib
import json
import jwt

from timer_data.db import User
from timer_data.encoders import TimerEncoder

SECRET = 'secret'  # TODO: make more valid secret and set it to the env
ALGORITHM = 'HS256'


def encode_user_password(pwd: str) -> str:
    return str(hashlib.sha256(
        ''.join(str(x) + str(y) for x in SECRET for y in pwd).encode()
    ).hexdigest())


def encode_token(user: User) -> str:
    return jwt.encode(
        {
            'username': user.username,
            'id': user.id
        },
        SECRET,
        algorithm=ALGORITHM
    )


def decode_token(token: str) -> dict:
    return jwt.decode(
        token,
        SECRET,
        algorithms=[ALGORITHM]
    )


def dump_timer(data):
    return json.dumps(data, cls=TimerEncoder)

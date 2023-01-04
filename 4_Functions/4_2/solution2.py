from json import dumps
from functools import wraps


def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return dumps(func(*args, **kwargs))

    return wrapper


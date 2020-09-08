from flask import request
from models.interns import Interns


def intern_route(user_id):
    # register intern
    if request.method == 'POST':
        content = request.get_json()
        interns = Interns()
        return interns.register_intern(content)

    # update intern info using user_id
    elif request.method == 'PUT':
        content = request.get_json()
        interns = Interns()
        return interns.update_intern(user_id, content)

    # get intern info using user_id
    elif request.method == 'GET':
        interns = Interns()
        return interns.get_intern(user_id)

    # delete intern using user_id
    else:
        interns = Interns()
        return interns.delete_intern(user_id)

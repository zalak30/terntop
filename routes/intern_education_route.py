from flask import request
from models.education import Education


def intern_education_route(user_id):
    if request.method == 'POST':
        content = request.get_json()
        education = Education()
        return education.add_education(user_id, content)
    # elif request.method == 'GET':
    #     education = Education()
    #     return education.get_education(user_id)
    # elif request.method == 'PUT':
    #     content = request.get_json()
    #     education = Education()
    #     return education.update_education(user_id, content)
    # else:
    #     content = request.get_json()
    #     education = Education()
    #     return education.delete_education(user_id, content)

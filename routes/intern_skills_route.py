from flask import request
from models.skills import Skills


def intern_skill_route(user_id):
    if request.method == 'POST':
        content = request.get_json()
        skills = Skills()
        return skills.add_skills(user_id, content)
    elif request.method == 'PUT':
        content = request.get_json()
        skills = Skills()
        return skills.update_skills(user_id, content)
    elif request.method == 'GET':
        skills = Skills()
        return skills.get_skills(user_id)
    else:
        content = request.get_json()
        skills = Skills()
        return skills.delete_skills(user_id, content)

from flask import Flask
from routes.intern_route import intern_route
from routes.intern_skills_route import intern_skill_route

app = Flask(__name__)


@app.route('/intern/<user_id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/intern/', defaults={'user_id': None}, methods=['POST'])
def intern(user_id):
    return intern_route(user_id)


@app.route('/intern/<user_id>/skills', methods=['GET', 'POST', 'PUT', 'DELETE'])
def skills(user_id):
    return intern_skill_route(user_id)


app.run(debug=True)

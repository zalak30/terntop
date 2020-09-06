from flask import Flask
from flask import request
from models.interns import Interns

app = Flask(__name__)


# api for intern information.
@app.route('/intern/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def personal_info(user_id):
    if request.method == 'PUT':
        content = request.get_json()
        return Interns.update_intern(user_id, content)

    elif request.method == 'GET':
        return Interns.get_intern(user_id)

    else:
        return Interns.delete_intern(user_id)


# api for intern registration.
@app.route('/intern', methods=['POST'])
def register_info():
    if request.method == 'POST':
        content = request.get_json()
        return Interns.register_intern(content)


app.run(debug=True)

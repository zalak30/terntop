from flask import Flask
from flask import request
from conn import Connection
from models.intern import Interns

app = Flask(__name__)


# api for user information.
@app.route('/user/<user_id>', methods=['GET', 'POST', 'PUT'])
def personal_info(user_id):
    if request.method == 'PUT':
        content = request.get_json()
        return Interns.update_intern(user_id, content)

    elif request.method == 'GET':
        return Interns.get_intern(user_id)


app.run(debug=True)

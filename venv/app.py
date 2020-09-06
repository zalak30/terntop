from flask import Flask
from flask import request
from models.interns import Interns

app = Flask(__name__)


# api for intern information.
@app.route('/intern/<user_id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/intern/', defaults={'user_id': None}, methods=['POST'])
def personal_info(user_id):
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


app.run(debug=True)

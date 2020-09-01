from flask import Flask
from flask import request, jsonify


app = Flask(__name__)


@app.route('/user', methods=['get'])
def create_cm():
    first_name = request.args.get('first_name', None)
    last_name = request.args.get('last_name', None)
    return first_name+' '+last_name


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


app.run(debug=True)

from flask import Flask
from flask import request, jsonify
import mysql.connector

app = Flask(__name__)


@app.route('/user', methods=['get'])
def create_cm():
    fname = request.args.get('fname', None)
    lname = request.args.get('lname', None)

    return fname+' '+lname


app.run(debug=True)

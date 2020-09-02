from flask import Flask
from flask import request
from conn import Connection

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def create_cm():
    if request.method == 'POST':
        obj = Connection()
        content = request.get_json()
        print(content)
        obj.cursor.execute("USE terntop")
        First_name = content['first_name']
        Last_name = content['last_name']
        obj.cursor.execute("INSERT INTO interns(first_name, last_name) VALUES (%s, %s)", (First_name, Last_name))
        obj.conn.commit()
        obj.close()
        return {'status': 200, 'message': 'User registered successfully..'}
    elif request.method == 'GET':
        obj = Connection()
        obj.cursor.execute("USE terntop")
        uid = request.args.get('uid')
        obj.cursor.execute("SELECT first_name, last_name FROM interns WHERE id = {}".format(uid))
        user = obj.cursor.fetchone()
        print(user)
        row_header = [x[0] for x in obj.cursor.description]
        print(row_header)
        obj.conn.commit()
        obj.close()

        if user is not None:
            return {'status': 200, 'data': dict(zip(row_header, user))}
        else:
            return 'user not found'


app.run(debug=True)

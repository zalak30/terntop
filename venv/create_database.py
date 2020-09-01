from conn import Connection

obj = Connection()
obj.conn_sql()

try:
    obj.sql_cursor.execute("CREATE DATABASE top")
    print('database created successfully')
except Exception as e:
    print(str(e))

obj.close_sql()

import mysql.connector
import credential


class Connection:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host=credential.host,
                user=credential.user,
                passwd=credential.passwd
            )
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                print('connection is established')
        except Exception as e:
            print("Error: ", str(e))

    def close(self):
        try:
            if self.conn.is_connected():
                self.cursor.close()
                self.conn.close()
                print('connection is closed')
        except Exception as e:
            print("Error", str(e))

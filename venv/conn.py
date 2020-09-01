import mysql.connector


class Connection:
    def conn_sql(self):
        try:
            self.sql_conn = mysql.connector.connect(
                host="localhost",
                user="zalak",
                passwd="6477132872"
            )
            if self.sql_conn.is_connected():
                self.sql_cursor = self.sql_conn.cursor()
                print('sql connection connected')
                print('sql cursor connected')
        except Exception as e:
            print(str(e))

    def conn_database(self):
        try:
            self.database_conn = mysql.connector.connect(
                host="localhost",
                user="zalak",
                passwd="6477132872",
                database="terntop"
            )
            if self.database_conn.is_connected():
                self.database_cursor = self.database_conn.cursor()
                print('database connection connected')
                print('database cursor connected')
        except Exception as e:
            print(str(e))

    def close_database(self):
        try:
            if self.database_conn.is_connected():
                self.database_cursor.close()
                self.database_conn.close()
                print('database connection closed')
        except Exception as e:
            print(str(e))

    def close_sql(self):
        try:
            if self.sql_conn.is_connected():
                self.sql_cursor.close()
                self.sql_conn.close()
                print('sql connection closed')
        except Exception as e:
            print(str(e))

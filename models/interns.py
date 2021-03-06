from conn import Connection
from datetime import datetime
import hashlib, uuid


class Interns:
    def __init__(self):
        # connect to database
        self.connection = Connection()
        self.connection.connect_database()

    def exists(self, user_id):
        # get user_id exists or not
        query = "SELECT user_id FROM interns WHERE user_id = '{}'".format(user_id)
        self.connection.cursor.execute(query)
        user_id = self.connection.cursor.fetchone()
        print(user_id)

        if user_id is None:
            return False
        else:
            return True

    # register intern
    def register_intern(self, content):
        print(content)

        try:
            user_id = content['user_id']
            pw = content['pw']
            date_registered = datetime.now()
            # pw to hash
            hash_pw = hashlib.sha256(str(pw).encode('utf-8')).hexdigest()

            if self.exists(user_id):
                payload = "user_id already registered", 200
                print(payload)
                return payload

            else:
                query = "INSERT INTO interns (user_id, pw_hash, date_registered) VALUES (%s, %s, %s)"
                values = (user_id, hash_pw, date_registered)
                self.connection.cursor.execute(query, values)

                payload = "Intern registered successfully", 200
                print(payload)
                return payload

        except Exception as e:
            payload = "Error : " + str(e), 500
            print(payload)
            return payload

        finally:
            self.connection.conn.commit()
            self.connection.close()

    # update intern's info using user_id
    def update_intern(self, user_id, content):
        print(content)

        if self.exists(user_id):
            try:
                email_id = content['email_id']
                first_name = content['first_name']
                last_name = content['last_name']
                full_name = first_name + ' ' + last_name
                image_url = content['image_url']
                phone = content['phone']
                country_code = content['country_code']
                city = content['city']
                state = content['state']
                country = content['country']
                date_updated = datetime.now()

            except Exception as e:
                payload = "invalid" + str(e), 500
                print(payload)
                return payload

            query = "UPDATE interns SET" \
                    " email_id = %s," \
                    " first_name = %s," \
                    " last_name = %s," \
                    " full_name = %s," \
                    " image_url = %s, " \
                    " phone = %s," \
                    " country_code = %s," \
                    " city = %s," \
                    " state = %s," \
                    " country = %s," \
                    " date_updated = %s" \
                    " WHERE user_id = %s"

            values = (
                email_id,
                first_name,
                last_name,
                full_name,
                image_url,
                phone,
                country_code,
                city,
                state,
                country,
                date_updated,
                user_id
            )

            try:
                self.connection.cursor.execute(query, values)
                self.connection.conn.commit()
                self.connection.close()
                payload = "Intern updated successfully", 200
                print(payload)
                return payload

            except Exception as e:
                payload = "Error : " + str(e), 500
                print(payload)
                return payload

        else:
            self.connection.close()
            payload = "Intern not registered", 200
            print(payload)
            return payload

    # get intern using user_id
    def get_intern(self, user_id):

        try:
            if self.exists(user_id):
                query = "SELECT * FROM interns WHERE user_id = '{}'".format(user_id)
                print(query)
                self.connection.cursor.execute(query)
                user = self.connection.cursor.fetchone()
                print(user)

                # getting needed row headers.
                row_header = [x[0] for x in self.connection.cursor.description]
                print(row_header)
                payload = {'status': 200, 'data': dict(zip(row_header, user))}
                print(payload)
                return payload
            else:
                payload = 'Intern not found'
                print(payload)
                return payload

        except Exception as e:
            payload = "Error : " + str(e), 500
            print(payload)
            return payload

        finally:
            self.connection.conn.commit()
            self.connection.close()

    # delete intern using user_id
    def delete_intern(self, user_id):

        try:
            if self.exists(user_id):
                query = "DELETE FROM interns WHERE user_id = '{}'".format(user_id)
                print(query)
                self.connection.cursor.execute(query)
                payload = "Intern deleted successfully", 200
                print(payload)
                return payload
            else:
                payload = "Intern not found", 200
                print(payload)
                return payload

        except Exception as e:
            payload = "Error : " + str(e), 500
            print(payload)
            return payload

        finally:
            self.connection.conn.commit()
            self.connection.close()

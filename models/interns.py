from conn import Connection


class Interns:
    @staticmethod
    def register_intern(content):
        connection = Connection()
        connection.connect_database()
        print(content)

        # get existing user_ids
        query = "SELECT user_id FROM interns"
        connection.cursor.execute(query)
        user_ids = connection.cursor.fetchall()

        # append existing user_ids into empty list
        existing_user_ids = []
        for user_id in user_ids:
            existing_user_ids.append(user_id[0])
        print(existing_user_ids)

        try:
            user_id = content['user_id']
            pw_hash = content['pw_hash']

            if user_id in existing_user_ids:
                payload = "user_id already registered"
                print(payload)
                return payload

            else:
                query = "INSERT INTO interns (user_id, pw_hash) VALUES (%s, %s)"
                values = (user_id, pw_hash)
                connection.cursor.execute(query, values)

                payload = "Intern registered successfully", 200
                print(payload)
                return payload

        except Exception as e:
            payload = "Error : " + str(e), 500
            print(payload)
            return payload

        finally:
            connection.conn.commit()
            connection.close()

    @staticmethod
    def update_intern(user_id, content):
        print(content)
        connection = Connection()
        connection.connect_database()

        try:
            first_name = content['first_name']
            last_name = content['last_name']
            full_name = first_name + ' ' + last_name
            image_url = content['image_url']
            phone = content['phone']
            country_code = content['country_code']
            city = content['city']
            state = content['state']
            country = content['country']

        except Exception as e:
            payload = "invalid" + str(e), 500
            print(payload)
            return payload

        query = "UPDATE interns SET" \
                " first_name = %s," \
                " last_name = %s," \
                " full_name = %s," \
                " image_url = %s, " \
                " phone = %s," \
                " country_code = %s," \
                " city = %s," \
                " state = %s," \
                " country = %s" \
                " WHERE user_id = %s"

        values = (
            first_name,
            last_name,
            full_name,
            image_url,
            phone,
            country_code,
            city,
            state,
            country,
            user_id
        )
        try:
            connection.cursor.execute(query, values)
            connection.conn.commit()
            connection.close()

            payload = "Intern updated successfully", 200
            print(payload)
            return payload

        except Exception as e:
            payload = "Error : " + str(e), 500
            print(payload)
            return payload

    @staticmethod
    def get_intern(user_id):
        connection = Connection()
        connection.connect_database()

        try:
            query = "SELECT * FROM interns WHERE user_id = '{}'".format(user_id)
            connection.cursor.execute(query)
            user = connection.cursor.fetchone()
            row_header = [x[0] for x in connection.cursor.description]
            connection.conn.commit()
            connection.close()

            if user is not None:
                return {'status': 200, 'data': dict(zip(row_header, user))}
            else:
                return 'user not found'

        except Exception as e:
            payload = "Error : " + str(e), 500
            print(payload)
            return payload

    @staticmethod
    def delete_intern(user_id):
        connection = Connection()
        connection.connect_database()

        try:
            query = "DELETE FROM interns WHERE user_id = '{}'".format(user_id)
            connection.cursor.execute(query)
            user = connection.cursor.fetchone()
            connection.conn.commit()
            connection.close()

            if user is not None:
                payload = "Intern deleted successfully", 200
                print(payload)
                return payload
            else:
                return 'user not found'

        except Exception as e:
            payload = "Error : " + str(e), 500
            print(payload)
            return payload

from conn import Connection


class Skills:
    def __init__(self):
        self.connection = Connection()
        self.connection.connect_database()

    # check user exists or not
    def exists(self, user_id):
        query = "SELECT user_id FROM interns WHERE user_id = '{}'".format(user_id)
        self.connection.cursor.execute(query)
        user_id = self.connection.cursor.fetchone()
        print(user_id)

        if user_id is None:
            return False
        else:
            return True

    # get existing skills
    def current_skills(self, user_id):
        try:
            if self.exists(user_id):
                # now get existing skills from database.
                query = "SELECT skills FROM interns WHERE user_id = '{}'".format(user_id)
                self.connection.cursor.execute(query)
                existing_skills = self.connection.cursor.fetchone()

                # getting existing skills in tuple format, first convert into string then set.
                existing_skills = set(','.join(existing_skills).split(','))
                print("existing_skills get successfully")
                return existing_skills
            else:
                payload = 'Intern not found'
                print(payload)
                return payload

        except Exception as e:
            payload = "Error : " + str(e), 500
            print(payload)
            return payload

    # get all skills in json format
    def get_skills(self, user_id):
        try:
            if self.exists(user_id):
                query = "SELECT user_id, skills FROM interns WHERE user_id = '{}'".format(user_id)
                self.connection.cursor.execute(query)
                existing_skills = self.connection.cursor.fetchone()
                print("existing_skills", existing_skills)

                # getting needed row headers.
                row_header = [x[0] for x in self.connection.cursor.description]
                print("row_header", row_header)

                # display data in json format
                payload = {'status': 200, 'data': dict(zip(row_header, existing_skills))}
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

    # add skills
    def add_skills(self, user_id, content):
        # add skills
        try:
            if self.exists(user_id):
                try:
                    skills = content['skills']
                    # getting items in string format, will convert it into set.
                    requested_skills = set(skills.split(','))
                    print(requested_skills, type(requested_skills))
                    print("requested_skills get successfully")

                    # now we have only unique skills left, will convert into str.
                    skills = ','.join(requested_skills)
                    print("skills", skills, type(skills))

                    # add skill to database
                    query = "UPDATE interns SET" \
                            " skills = %s" \
                            " WHERE user_id = %s"
                    values = (skills, user_id)
                    self.connection.cursor.execute(query, values)
                    payload = "skills successfully added", 200
                    print(payload)
                    return payload

                except Exception as e:
                    payload = "Error " + str(e), 500
                    print(payload)
                    return payload

            else:
                payload = "user_id not exists", 200
                print(payload)
                return payload

        except Exception as e:
            payload = "Error " + str(e), 500
            print(payload)
            return payload

        finally:
            self.connection.conn.commit()
            self.connection.close()

    # update skills
    def update_skills(self, user_id, content):
        try:
            if self.exists(user_id):
                try:
                    skills = content['skills']
                    # getting items in string format, will convert it into set.
                    requested_skills = set(skills.split(','))
                    print("requested_skills get successfully")

                    # we have two sets one is existing skills and second is requested skills.
                    # to add skills in database it must be in string format.
                    new_skills = ','.join(set(self.current_skills(user_id)).union(set(requested_skills)))
                    print("new_skills  get successfully")

                    # add skills to database.
                    query = "UPDATE interns SET" \
                            " skills = %s" \
                            " WHERE user_id = %s"
                    values = (new_skills, user_id)
                    self.connection.cursor.execute(query, values)

                    payload = "skills successfully updated", 200
                    print(payload)
                    return payload

                except Exception as e:
                    payload = "Error " + str(e), 500
                    print(payload)
                    return payload

            else:
                payload = "user_id not exists", 200
                print(payload)
                return payload

        except Exception as e:
            payload = "Error " + str(e), 500
            print(payload)
            return payload

        finally:
            self.connection.conn.commit()
            self.connection.close()

    # delete skills
    def delete_skills(self, user_id, content):
        try:
            if self.exists(user_id):
                skills = content['skills']
                # getting items in string format, will convert it into set.
                requested_skills = set(skills.split(','))
                print(requested_skills)
                print("requested_skills get successfully")

                # get existing skills and from existing skills remove requested skills.
                existing_skills = self.current_skills(user_id)
                print("existing_skills", existing_skills)
                for requested_skill in requested_skills:
                    if requested_skill in existing_skills:
                        existing_skills.remove(requested_skill)

                        # to add skills in database it must be in string format.
                        new_skills = ','.join(set(existing_skills))
                        print("new_skills", new_skills)
                        print("new_skills  get successfully")

                        # add skills to database.
                        query = "UPDATE interns SET" \
                                " skills = %s" \
                                " WHERE user_id = %s"
                        values = (new_skills, user_id)
                        self.connection.cursor.execute(query, values)

                        payload = "skills deleted successfully", 200
                        print(payload)
                        return payload

                    else:
                        print("skill not listed")
            else:
                payload = "user_id not exists", 200
                print(payload)
                return payload

        finally:
            self.connection.conn.commit()
            self.connection.close()

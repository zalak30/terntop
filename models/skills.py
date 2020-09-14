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
        print("user_id: ", user_id)

        if user_id is None:
            return False
        else:
            return True

    # get existing skills
    def current_skills(self, user_id):
        # now get existing skills from database.
        query = "SELECT skills FROM interns WHERE user_id = '{}'".format(user_id)
        self.connection.cursor.execute(query)
        self.existing_skills = self.connection.cursor.fetchone()
        return self.existing_skills[0]

    # validation for empty skill and given information is in list format
    def skill_validation(self, content):
        try:
            self.skills = content['skills']

        except Exception as e:
            self.payload = "Error " + str(e), 500
            print(self.payload)
            return self.payload

        if type(self.skills) is not list:
            self.payload = "given argument must be in list format", 200
            print(self.payload)
            return self.payload

        if len(self.skills) == 0:
            self.payload = "list can not be empty", 200
            print(self.payload)
            return self.payload

        for skill in self.skills:
            length = len(skill.strip())

            if length == 0:
                self.payload = "skill can not be empty", 200
                print(self.payload)
                return self.payload

            if skill.isalnum() is False:
                self.payload = "only alphanumeric allowed", 200
                print(self.payload)
                return self.payload

    # get all skills in json format
    def get_skills(self, user_id):
        if self.exists(user_id):
            query = "SELECT user_id, skills FROM interns WHERE user_id = '{}'".format(user_id)
            try:
                self.connection.cursor.execute(query)
                existing_skills = self.connection.cursor.fetchone()
                print("existing_skills", existing_skills)

                # getting needed row headers.
                row_header = [x[0] for x in self.connection.cursor.description]
                print("row_header", row_header)
                self.connection.close()

                # display data in json format
                payload = {'status': 200, 'data': dict(zip(row_header, existing_skills))}
                print(payload)
                return payload
            except Exception as e:
                payload = "Error : " + str(e), 500
                print(payload)
                return payload
        else:
            self.connection.close()
            payload = 'Intern not found'
            print(payload)
            return payload

    # add skills
    def add_skills(self, user_id, content):
        # add skills
        if self.skill_validation(content):
            return self.payload

        if self.exists(user_id):
            # getting items in string format, will convert it into set.
            requested_skills = set(self.skills)
            print("requested_skills", requested_skills)
            print("requested_skills get successfully")

            # now we have only unique skills left, will convert into str.
            skills = ','.join(requested_skills)
            print("skills", skills, type(skills))

            try:
                # add skill to database
                query = "UPDATE interns SET skills = %s WHERE user_id = %s"
                values = (skills, user_id)
                self.connection.cursor.execute(query, values)
                self.connection.conn.commit()
                payload = "skills successfully added", 200
                print(payload)
                return payload

            except Exception as e:
                payload = "Error: " + str(e), 500
                print(payload)
                return payload

            finally:
                self.connection.close()

        else:
            self.connection.close()
            payload = "Intern not found", 404
            print(payload)
            return payload

    # update skills
    def update_skills(self, user_id, content):
        if self.skill_validation(content):
            return self.payload

        if self.exists(user_id):
            if self.current_skills(user_id) is None:
                payload = "nothing added in skills yet"
                print(payload)
                return payload
            else:
                # getting existing skills in tuple format, first convert into string then set.
                self.existing_skills = set(','.join(self.existing_skills).split(','))
                # getting items in list format, will convert it into set.
                requested_skills = set(self.skills)
                print("requested_skills get successfully")

                # we have two sets one is existing skills and second is requested skills.
                # to add skills in database it must be in string format.
                new_skills = ','.join(self.existing_skills.union(requested_skills))
                print("new_skills  get successfully")

                # add skills to database.
                query = "UPDATE interns SET skills = %s WHERE user_id = %s"
                values = (new_skills, user_id)
                try:
                    self.connection.cursor.execute(query, values)
                    self.connection.conn.commit()
                    payload = "skills successfully updated", 200
                    print(payload)
                    return payload
                except Exception as e:
                    payload = "Error: " + str(e), 500
                    print(payload)
                    return payload
                finally:
                    self.connection.close()

        else:
            self.connection.close()
            payload = "'Intern not found'", 404
            print(payload)
            return payload

    # delete skills
    def delete_skills(self, user_id, content):
        if self.skill_validation(content):
            return self.payload

        if self.exists(user_id):
            if self.current_skills(user_id) is None:
                payload = "nothing added in skills yet"
                print(payload)
                return payload
            else:
                # getting existing skills in tuple format, first convert into string then set.
                self.existing_skills = set(','.join(self.existing_skills).split(','))
                # getting items in string format, will convert it into set.
                requested_skills = set(self.skills)
                print("requested_skills get successfully")

                # from existing skills remove requested skills.
                payload = []
                for requested_skill in requested_skills:
                    if requested_skill in self.existing_skills:
                        self.existing_skills.remove(requested_skill)

                        # to add skills in database it must be in string format.
                        new_skills = ','.join(set(self.existing_skills))
                        print("new_skills", new_skills)
                        print("new_skills  get successfully")

                        # add skills to database.
                        query = "UPDATE interns SET skills = %s WHERE user_id = %s"
                        values = (new_skills, user_id)
                        try:
                            self.connection.cursor.execute(query, values)
                            self.connection.conn.commit()
                            payload = "skills deleted successfully " + requested_skill,  200
                            print(payload)
                        except Exception as e:
                            payload = "Error: " + str(e), 500
                            print(payload)
                            return payload
                        finally:
                            self.connection.close()

                    else:
                        payload = "skill not listed " + requested_skill, 404
                        print(payload)
                return payload

        else:
            self.connection.close()
            payload = "Intern not found", 404
            print(payload)
            return payload

from conn import Connection
from models.skills import Skills
import uuid

# to check user is exists or not, import function "skill_validation" from "Skills" class
skills = Skills()


class Education:
    def __init__(self):
        self.connection = Connection()
        self.connection.connect_database()

    def education_validation(self, content):
        try:
            self.content = content

            for edu in self.content:
                # check dictionary is empty or not
                if not edu:
                    self.payload = "dictionary can not be empty", 200
                    return self.payload

                if type(edu['type']) is not str:
                    self.payload = "degree type must be string", 200
                    return self.payload

                if type(edu['name']) is not str:
                    self.payload = "degree name must be string", 200
                    return self.payload
                if type(edu['is_completed']) is not bool:
                    self.payload = "is_completed must be boolean", 200
                    return self.payload
                if type(edu['year']) is not list:
                    self.payload = "degree year must be list", 200
                    return self.payload
                # check year is int or not
                for year in edu['year']:
                    if type(year) is not int:
                        self.payload = "degree year must be int", 200
                        return self.payload
                    if len(edu['year']) > 2:
                        self.payload = 'year exceeds the maximum allowed length of 2', 200
                        return self.payload

        except Exception as e:
            payload = "Error : " + str(e), 500
            print(payload)
            return payload

    def add_education(self, user_id, content):
        if self.education_validation(content):
            return self.payload
        if skills.exists(user_id):
                query = "UPDATE interns SET education = %s WHERE user_id = %s"
                values = (str(self.content), user_id)
                try:
                    self.connection.cursor.execute(query, values)
                    self.connection.conn.commit()
                    self.connection.close()
                    payload = "education successfully updated", 200
                    print(payload)
                    return payload
                except Exception as e:
                    payload = "Error : " + str(e), 500
                    print(payload)
                    return payload

        else:
            payload = "intern not found", 200
            print(payload)
            return payload

    def get_education(self, user_id):
        query = "SELECT user_id, education FROM interns WHERE user_id = '{}'".format(user_id)
        self.connection.cursor.execute(query)
        existing_education = self.connection.cursor.fetchone()
        print("existing_education : ", existing_education)

        row_header = [x[0] for x in self.connection.cursor.description]
        print("row_header : ", row_header)
        self.connection.close()
        payload = {'status': 200, 'data': dict(zip(row_header, existing_education))}
        print(payload)
        return payload

# def update_education(self, user_id, content):
#

# def delete_education(self, user_id, content):
#


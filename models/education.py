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
            self.education = content['education']
        except Exception as e:
            self.payload = "Error : " + str(e), 500
            print(self.payload)
            return self.payload

        if type(self.education) is not list:
            self.payload = "education must be in list format"
            print(self.payload)
            return self.payload

        # check dictionary is empty or not
        if len(self.education) == 0:
            self.payload = "list can not be empty", 200
            print(self.payload)
            return self.payload

        allowed_chars = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_ ")

        for dict in self.education:
            print("dic : ", dict)
            if not dict:
                self.payload = "dictionary keys can not be empty"
                print(self.payload)
                return self.payload
            for key, value in dict.items():
                print("key : ", key)
                print("value : ", value)

                if set(str(key)).issubset(allowed_chars) is False:
                    self.payload = "accept only alphanumeric and underscore(_)"
                    print(self.payload)
                    return self.payload
                if set(str(value)).issubset(allowed_chars) is False:
                    self.payload = "accept only alphanumeric and underscore(_)"
                    print(self.payload)
                    return self.payload

        # values = self.education.values()
        # for value_list in values:
        #     if type(value_list) is not list:
        #         self.payload = "values must be in list"
        #         print(self.payload)
        #         return self.payload
        #     for value in value_list:
        #         print(value)
        #         length = len(str(value).split())
        #         print(length)
        #         if length == 0:
        #             self.payload = "dictionary values can not be empty"
        #             print(self.payload)
        #             return self.payload
        #         if set(str(value)).issubset(allowed_chars) is False:
        #             self.payload = "accept only alphanumeric and underscore(_)"
        #             print(self.payload)
        #             return self.payload

    def add_education(self, user_id, content):
        # if self.education_validation(content):
        #     return self.payload
        if skills.exists(user_id):
            try:
                type = content['type'],
                name = content['name'],
                year = content['year'],
                is_completed = content['is_completed'],
                # create unique id for each degree
                id = uuid.uuid4().node

                # my_dict = {
                #     "type": type,
                #     "name": name,
                #     "year": year,
                #     "is_completed": is_completed,
                #     # create unique id for each degree
                #     "id": id
                # }
                #
                # # convert dictionary to string as insert into database.
                # str_dict = str(my_dict)
                print(type, name, year, is_completed, id)
                return type, name, year, is_completed, id
            except Exception as e:
                payload = "Error : ", str(e)
                print(payload)
                return payload

            # query = "UPDATE interns SET education = %s WHERE user_id = %s"
            # values = (str_dict, user_id)
            # try:
            #     self.connection.cursor.execute(query, values)
            #     self.connection.conn.commit()
            #     self.connection.close()
            #     payload = "education successfully updated", 200
            #     print(payload)
            #     return payload
            # except Exception as e:
            #     payload = "Error : " + str(e), 500
            #     print(payload)
            #     return payload

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

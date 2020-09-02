from conn import Connection

# create object for class "Connection"
obj = Connection()

# create database "terntop"
try:
    obj.cursor.execute("CREATE DATABASE terntop")
    print('database created successfully')
except Exception as e:
    print('Error: ', str(e))


# connect to sql database "terntop"
obj.cursor.execute("USE terntop")

# create table "interns"
try:
    obj.cursor.execute("CREATE TABLE interns (id INT AUTO_INCREMENT PRIMARY KEY, pw_hash VARCHAR(100),"
                       "first_name VARCHAR(10), last_name VARCHAR(10), "
                       "full_name VARCHAR(20), image_url TEXT,phone INT(10), country_code VARCHAR(2),"
                       "city VARCHAR(20), state VARCHAR(20), country VARCHAR(20), "
                       "date_registered TIMESTAMP, date_updated TIMESTAMP,"
                       "skills TEXT, education TEXT, experience TEXT, applications TEXT)")
    print('"interns" table created successfully')
except Exception as e:
    print(str(e))

# create table "employers"
try:
    obj.cursor.execute("CREATE TABLE employers (id INT AUTO_INCREMENT PRIMARY KEY, pw_hash VARCHAR(100),"
                       "first_name VARCHAR(10), last_name VARCHAR(10), full_name VARCHAR(20), image_url TEXT,"
                       "phone INT(10), country_code VARCHAR(2), city VARCHAR(20), state VARCHAR(20),"
                       "country VARCHAR(20), date_registered TIMESTAMP, date_updated TIMESTAMP,"
                       "company_name VARCHAR(40), company_website TEXT, company_about TEXT, jobs TEXT)")
    print('"employers" table created successfully')
except Exception as e:
    print(str(e))

# close the connection
obj.close()

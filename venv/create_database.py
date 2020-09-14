from conn import Connection

# create object for class "Connection"
connection = Connection()

# create database "terntop"
try:
    connection.cursor.execute("CREATE DATABASE terntop")
    print('database created successfully')
except Exception as e:
    print('Error: ', str(e))

# connect to sql database "terntop"
connection.connect_database()

# create table "interns"
try:
    connection.cursor.execute(
        "CREATE TABLE interns (user_id VARCHAR(10) NOT NULL UNIQUE PRIMARY KEY, "
        "email_id VARCHAR(50), pw_hash VARCHAR(100) NOT NULL, "
        "first_name VARCHAR(20), last_name VARCHAR(40), full_name VARCHAR(20),"
        "image_url TEXT,phone BIGINT(10),country_code VARCHAR(2), city VARCHAR(20),"
        "state VARCHAR(20), country VARCHAR(20) ,date_registered TIMESTAMP, "
        "date_updated TIMESTAMP, skills TEXT, education TEXT,"
        "experience TEXT, applications TEXT)"
    )
    print('"interns" table created successfully')
except Exception as e:
    print(str(e))

# create table "employers"
try:
    connection.cursor.execute(
        "CREATE TABLE employers (user_id VARCHAR(10) NOT NULL UNIQUE PRIMARY KEY,"
        "email_id VARCHAR(50), pw_hash VARCHAR(100) NOT NULL, first_name VARCHAR(20),"
        "last_name VARCHAR(20), full_name VARCHAR(40), image_url TEXT, phone BIGINT(10) NOT NULL,"
        "country_code VARCHAR(2), city VARCHAR(20), state VARCHAR(20),"
        "country VARCHAR(20), date_registered TIMESTAMP, date_updated TIMESTAMP,"
        "company_name VARCHAR(40), company_website TEXT NOT NULL,"
        "company_about TEXT, jobs TEXT)"
    )
    print('"employers" table created successfully')
except Exception as e:
    print(str(e))

# close the connection
connection.close()

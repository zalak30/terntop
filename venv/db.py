host = "localhost"
user = "zalak"
passwd = "6477132872"

mydb = mysql.connector.connect(
        host=db.host,
        user=db.user,
        passwd=db.passwd,
)
print(mydb)

mycursor = mydb.cursor()
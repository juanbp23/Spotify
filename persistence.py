import mysql.connector

cnx = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Chamartin23*",
  database="Spotify"
)

query = ("SELECT name FROM user")
cursor = cnx.cursor()
cursor.execute(query)
names_user = []
for i in cursor:
    names_user.append(i)
sa
import mysql.connector as mariadb

mariadb_user = "root"
mariadb_pwd = ""



app = mariadb.connect(host='localhost', user=mariadb_user, password=mariadb_pwd)
curseur = app.cursor()
curseur.execute("USE app")
curseur.execute("SELECT * FROM users") 
noms = []
for row in :
    nom = row[0]
    noms.append(nom)
    app.commit()
    curseur.close()
    app.close()
  

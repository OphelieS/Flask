from flask import Flask, render_template, request, flash, session 
import mysql.connector as mariadb
app = Flask(__name__)

mariadb_user = "root"
mariadb_pwd = ""
app.secret_key = "super secret key"

@app.route("/")
def hello():
    return render_template("home.html", message_home = "Bienvenue sur la page d'accueil !")

@app.route('/', methods=['POST'])
def text_box():
    text = request.form['username']
    processed_text = text.upper()
    return render_template("bienvenue.html", message=processed_text)


@app.route("/next")
def suite():
    return render_template("page_suivante.html")

@app.route("/formulaire")
def form():
    return render_template("formulaire.html")

@app.route("/formulaire", methods=["POST"])
def formu():
    prenom = request.form["prenom"]
    nom = request.form["nom"]
    sexe = request.form["sexe"]
    pseudo = request.form["pseudo"]

    app = mariadb.connect(host='localhost', user=mariadb_user, password=mariadb_pwd)
    curseur = app.cursor()
    curseur.execute("CREATE DATABASE IF NOT EXISTS app")
    curseur.execute("USE app")
    curseur.execute("CREATE TABLE IF NOT EXISTS users (prenom VARCHAR(255), nom VARCHAR(255), sexe ENUM('M.', 'Mme'), pseudo VARCHAR(255), unique(pseudo))")
    try: 
        curseur.execute(f"INSERT INTO users VALUES ('{prenom}', '{nom}', '{sexe}', '{pseudo}')")
        app.commit()
        flash(" Merci d'avoir créé votre compte :-)")
        return render_template("bonjour.html", sexe = sexe,prenom = prenom, nom = nom, pseudo = pseudo)
    except :
        flash("Merci de choisir un autre pseudo, celui-ci existe déjà :-)")
        return render_template("formulaire.html")

@app.route("/base")
def liste():
    app = mariadb.connect(host='localhost', user=mariadb_user, password=mariadb_pwd)
    curseur = app.cursor()
    curseur.execute("USE app")
    curseur.execute("""SELECT nom, prenom,sexe, pseudo FROM users""")
    user1 = curseur.fetchall()
    app.commit()
    curseur.close()
    app.close()
    return render_template("base.html", user1= user1,contact = user1)

@app.route("/stat")
def stat():
    return render_template("stat.html")

@app.route("/mnist")
def mnist():
    return render_template("mnist.html")


if __name__ == "__main__":
    app.run(debug=True)

    #recuperer qqs images mnist, extension sav, mon model.predict(nouvelle image)
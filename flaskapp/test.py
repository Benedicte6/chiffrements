from flask import Flask, request, render_template, redirect, url_for
import datetime
import base
import RSA
import mysql.connector

app=Flask(__name__)

@app.route('/')
def connexion():
    return render_template('connexion.html')

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db=base.connector()
        cursor = db.cursor()
        cursor.execute("INSERT INTO utilisateur (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
    return redirect(url_for('accueil'))    

@app.route('/accueil')
def accueil():
    db = base.connector()
    cursor =db.cursor()
    req= "SELECT * FROM etudiant"
    cursor.execute(req)
    data = cursor.fetchall()
    return render_template("index.html",data=data)


@app.route('/ajouter', methods=['POST'])
def ajouter_etudiant():
    donnees=request.form
    nom = donnees.get('nom')
    name_crypted = RSA.rsa(nom,33,3)
    matricule = donnees.get('matricule')
    postnom= donnees.get('postnom')
    postname_crypted = RSA.rsa(postnom,33,3)
    dateNaissance = donnees.get('dateNaissance')
    print(matricule,nom,postnom,dateNaissance)

    db=base.connector()
    cursor=db.cursor()
    sql="insert into etudiant (matricule, nom ,postnom,dateNaissance) VALUES (%s,%s,%s,%s)"
    valeurs= (matricule,name_crypted,postname_crypted,datetime.date.today())
    cursor.execute(sql,valeurs)
    db.commit()
    return redirect(url_for('accueil'))
     

@app.route('/to_save_std') 
def formulaire():
    return render_template('formulaire.html') 

# Modifier un étudiant
@app.route('/Ouvrir_Modifier/<matricule>/')
def modifier_etudiant(matricule):
    db=base.connector()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM etudiant WHERE matricule = %s", (matricule,))
    data=cursor.fetchall()
    db.commit()
    return render_template('update.html', data=data)

@app.route('/update/<matricule>',methods=['POST'])
def update(matricule):
    if request.method == 'POST':
        nom=request.form['nom']
        postnom=request.form['postnom']
        date=request.form['dateNaissance']
        values=(nom, postnom, date,matricule)
        print(values)
        req = 'UPDATE etudiant SET nom=%s,postnom=%s,dateNaissance=%s WHERE matricule=%s'
        db = base.connector()
        cursor=db.cursor()
        cursor.execute(req,values)
        db.commit()
        return redirect(url_for('accueil'))
         

# Supprimer un étudiant
@app.route('/delete/<matricule>/')
def supprimer_etudiant(matricule):
    db=base.connector()
    cursor = db.cursor()
    cursor.execute("DELETE FROM etudiant WHERE matricule = %s", (matricule,))
    db.commit()
    return redirect(url_for('accueil'))
        

@app.route('/heure')
def heure():
    date_heure = datetime.datetime.now()
    h = date_heure.hour
    m = date_heure.minute
    s = date_heure.second
    return render_template("heure.html",heure = h, minute= m, second=s) 

    

if __name__== '__main__':
    app.run(debug=True)



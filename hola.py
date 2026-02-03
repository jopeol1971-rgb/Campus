from flask import Flask, render_template, request   
<<<<<<< HEAD
from psycopg2 import connect
=======
>>>>>>> origin/main

app = Flask(__name__)

def conectarCampus():
    conexion = connect(dbname="campus", user="postgres", password="1234", host="localhost", port="5432")
    print(f'La base de datos esta conectada: {conexion.status}') # si es 1, esta conectada
    return conexion


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        usuario = request.form["user"]
        password = request.form["password"]
        email = request.form["email"]
<<<<<<< HEAD
        
        conn = conectarCampus()
        cursor = conn.cursor() 
        cursor.execute("INSERT INTO usuarios ( usuario, password, email) VALUES ( %s, %s, %s)", (usuario, password, email))
        conn.commit()
        cursor.close()      
        conn.close()
    
        
        return render_template("user.html", usuario=usuario, email=email)
=======
        color = request.form["color"]

        print("Usuario ingresado:", usuario)
        print("Contraseña ingresada:", password)
        return render_template("user.html", usuario=usuario, email=email, color=color)
>>>>>>> origin/main
    
    return render_template("login.html")




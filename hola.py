from flask import Flask, render_template, request   
from psycopg2 import connect

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
        
        conn = conectarCampus()
        cursor = conn.cursor() 
        cursor.execute("INSERT INTO usuarios ( usuario, password, email) VALUES ( %s, %s, %s)", (usuario, password, email))
        conn.commit()
        cursor.close()      
        conn.close()
    
        
        return render_template("user.html", usuario=usuario, email=email)
    
    return render_template("login.html")




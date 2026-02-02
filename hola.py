from flask import Flask, render_template, request   

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        usuario = request.form["user"]
        password = request.form["password"]
        email = request.form["email"]
        color = request.form["color"]

        print("Usuario ingresado:", usuario)
        print("Contraseña ingresada:", password)
        return render_template("user.html", usuario=usuario, email=email, color=color)
    
    return render_template("login.html")




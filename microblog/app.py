#python -m venv venv
#.\venv\Scripts\activate
#pip install flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html", tel="(87) 988889898", nome="Joao")

@app.route("/operacao/<int:num1>/<int:num2>")
def somar_numeros(num1, num2):
     return f"O resultado da soma é: {num1 + num2}"
   
if __name__ == '__main__':
    app.run()

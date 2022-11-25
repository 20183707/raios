import numpy as np
from flask import Flask, render_template, request
import mysql.connector # importando la libreria para la base de datos
import ast

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template("mostrarAlumnos.html")





@app.route('/procesarAlumnos', methods=['POST'])
def procesarAlumnos():

    palabra = request.form.get("nombre")


    with open('miInvertido.txt', "r", encoding="utf8") as f:
        data = f.read()

        diccionario = ast.literal_eval(data)

    recuperar = []
    print("\n\n")
    for key, values in diccionario.items():
        if palabra in key:
            recuperar.append([key, values])




    idiomas = ["Ingles", "Español", "Frances"]

    return render_template("mostrarAlumnos.html", palabra = palabra, recuperar = recuperar, idiomas = idiomas)



if __name__=='__main__':
    app.run(debug=True)
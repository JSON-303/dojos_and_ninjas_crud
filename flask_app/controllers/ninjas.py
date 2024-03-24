from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask import render_template, redirect, request


@app.get("/")
@app.get("/ninjas")
def all_ninjas():
    ninjas = Ninja.all_ninjas()
    return render_template("all_ninjas.html", ninjas=ninjas)


@app.get("/ninjas/new")
def create_ninja():
    dojos = Dojo.all_dojos()
    return render_template("add_ninja.html", dojos=dojos)


@app.post("/ninjas/new")
def create_new_ninja():
    dojo_id = request.form["dojo"]
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    age = request.form["age"]

    ninja_data = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "dojo_id": dojo_id,
    }

    ninja_id = Ninja.create(ninja_data)
    print(ninja_id)

    return redirect(f"/dojos/{dojo_id}")

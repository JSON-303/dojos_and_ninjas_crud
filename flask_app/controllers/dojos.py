from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template, redirect, request


@app.route("/", methods=["GET", "POST"])
@app.route("/dojos", methods=["GET", "POST"])
def all_dojos():
    if request.method == "POST":
        name = request.form.get("name")
        success = Dojo.create_dojo({"name": name})
        if success:
            return redirect("/dojos")
        else:
            return "Failed to create dojo"
    else:
        dojos = Dojo.all_dojos()
        return render_template("all_dojos.html", dojos=dojos)


@app.get("/dojos/<int:dojo_id>")
def dojo_details(dojo_id):
    """This route displays one users' details"""

    dojo = Dojo.find_by_id_with_ninjas(dojo_id)
    if dojo == None:
        return "Cannont find Dojo."

    return render_template("dojo_details.html", dojo=dojo)

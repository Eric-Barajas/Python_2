from flask import Flask, render_template, request, redirect
from flask_app import app 
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo



#! CREATE
@app.route('/ninja/new')
def new_ninja():
    return render_template('create_ninja.html', dojos = Dojo.get_all())

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    # to retrive data from a form must use request.form instead of passing in data
    return redirect('/')

#! READ ALL
@app.route('/ninja')
def theninja():
    return render_template("read_ninja.html", ninjas = Ninja.get_all())

#! READ(ONE)
@app.route('/ninja/show/<int:id>')
def show_ninja(id):
    data = {'id': id}
    return render_template("show_ninja.html", ninja = Ninja.get_one(data))

#! UPDATE
@app.route('/ninja/edit/<int:id>')
def edit_ninja(id):
    data = {'id': id}
    return render_template('edit_ninja.html', ninja = Ninja.get_one(data))

@app.route('/ninja/update', methods = ['POST'])
def update_ninja():
    print(request.form)
    print("***************************")
    Ninja.update(request.form)
    return redirect('/')

#! DELETE
@app.route('/ninja/delete/<int:id>')
def delete_ninja(id):
    data = {'id': id}
    # when we have to pass in a number have to use a dictionary thingy above^^
    Ninja.destroy(data)
    return redirect('/')
from flask import Flask, render_template, request, redirect
from flask_app import app 
from flask_app.models.dojo import Dojo


#! CREATE
@app.route('/dojo/new')
def new_dojo():
    return render_template('create.html')

@app.route('/dojo/create', methods=['POST'])
def create_dojo():
    print(request.form)
    Dojo.save(request.form)
    # to retrive data from a form must use request.form instead of passing in data
    return redirect('/')

#! READ ALL
@app.route('/')
def index():
    return render_template("read.html", dojos = Dojo.get_all())

#! READ(ONE)
@app.route('/dojo/show/<int:id>')
def show_dojo(id):
    data = {'id': id}
    return render_template("show_dojo.html", dojo = Dojo.get_one_with_ninjas(data))

#! UPDATE
@app.route('/dojo/edit/<int:id>')
def edit_dojo(id):
    data = {'id': id}
    return render_template('edit_dojo.html', dojo = Dojo.get_one(data))

@app.route('/dojo/update', methods = ['POST'])
def update_dojo():
    print(request.form)
    print("***************************")
    Dojo.update(request.form)
    return redirect('/')

#! DELETE
@app.route('/delete/<int:id>')
def delete_dojo(id):
    data = {'id': id}
    # when we have to pass in a number have to use a dictionary thingy above^^
    Dojo.destroy(data)
    return redirect('/')

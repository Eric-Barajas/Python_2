from flask import Flask, render_template, request, redirect
from flask_app import app 
from flask_app.models.user import User

#! READ ALL
@app.route('/')
def index():
    return render_template("read.html", users = User.get_all())

#! CREATE
@app.route('/user/new')
def new_user():
    return render_template('create.html')

@app.route('/user/create', methods=['POST'])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/')



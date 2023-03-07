from flask import Flask, render_template, request, redirect
from flask_app import app 
from flask_app.models.user import User


# #! CREATE
# @app.route('/user/new')
# def new_user():
#     return render_template('create.html')

# @app.route('/user/create', methods=['POST'])
# def create_user():
#     print(request.form)
#     User.save(request.form)
#     # to retrive data from a form must use request.form instead of passing in data
#     return redirect('/')

#! READ ALL
@app.route('/')
def index():
    return render_template("user_home.html", users = User.get_all())

# #! READ(ONE)
# @app.route('/user/show/<int:id>')
# def show_user(id):
#     data = {'id': id}
#     return render_template("show_user.html", user = User.get_one(data))

# #! UPDATE
# @app.route('/user/edit/<int:id>')
# def edit_user(id):
#     data = {'id': id}
#     return render_template('edit_user.html', user = User.get_one(data))

# @app.route('/user/update', methods = ['POST'])
# def update_user():
#     print(request.form)
#     print("***************************")
#     User.update(request.form)
#     return redirect('/')

# #! DELETE
# @app.route('/delete/<int:id>')
# def delete_user(id):
#     data = {'id': id}
#     # when we have to pass in a number have to use a dictionary thingy above^^
#     User.destroy(data)
#     return redirect('/')
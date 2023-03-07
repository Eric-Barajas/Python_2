from flask import Flask, render_template, request, redirect
from flask_app import app 
from flask_app.models.recipe import Recipe
from flask_app.models.user import User



#! CREATE
@app.route('/recipe/new')
def new_recipe():
    return render_template('create_recipe.html', users = User.get_all())

@app.route('/recipe/create', methods=['POST'])
def create_recipe():
    print(request.form)
    Recipe.save(request.form)
    # to retrive data from a form must use request.form instead of passing in data
    return redirect('/')

#! READ ALL
@app.route('/recipe')
def therecipe():
    return render_template("read_recipe.html", recipes = Recipe.get_all())

#! READ(ONE)
@app.route('/recipe/show/<int:id>')
def show_recipe(id):
    data = {'id': id}
    return render_template("show_recipe.html", recipe = Recipe.get_one(data))

#! UPDATE
@app.route('/recipe/edit/<int:id>')
def edit_recipe(id):
    data = {'id': id}
    return render_template('edit_recipe.html', recipe = Recipe.get_one(data))

@app.route('/recipe/update', methods = ['POST'])
def update_recipe():
    print(request.form)
    print("***************************")
    Recipe.update(request.form)
    return redirect('/')

#! DELETE
@app.route('/recipe/delete/<int:id>')
def delete_recipe(id):
    data = {'id': id}
    # when we have to pass in a number have to use a dictionary thingy above^^
    Recipe.destroy(data)
    return redirect('/')
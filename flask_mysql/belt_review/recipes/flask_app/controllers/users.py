from flask_app import app, render_template, redirect, request, bcrypt, session, flash
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/things')
def signed_in():
    if "user_id" not in session:
        return redirect('/logout')
    # stops them from visiting certain route without being logged in
    return render_template('things.html')

#! CREATE AKA REGISTER
@app.route('/register', methods = ['POST'])
def register():
    print(request.form)
    user = User.get_by_email(request.form)
    print(user)
    if user:
        flash('email taken')
        return redirect('/')
    # TODO validate our user
    if not User.validate_user(request.form):
        return redirect('/')
    # TODO hash the password
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    print (hashed_pw)
    # TODO save the user to the datebase
    user_data ={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': hashed_pw,
        }
    user_id = User.save(user_data)
    # TODO log in the user
    session['user_id'] = user_id
    # putting them in session logs the user in
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    return redirect('/things')

#! READ and VERIFY AKA LOGIN

@app.route('/login', methods = ['POST'])
def login():
    # TODO see if the email is on our DB
    user = User.get_by_email(request.form)
    if not user:
        flash("incorrect email and/or password")
        return redirect('/')
    # TODO chech to see if the password matches the password in our DB
    password_valid = bcrypt.check_password_hash(user.password, request.form['password'])
    if not password_valid:
        flash("incorrect email and/or password")
        return redirect('/')
    # TODO log in the user
    session['user_id'] = user.id
    # have to use (.) instead of (_) because dot is to retrive info from the dateabse
    session['first_name'] = user.first_name
    session['last_name'] = user.last_name
    return redirect('/things')

#! LOGOUT

@app.route('/logout')
def logout():
    session.clear() 
    # to log the user out just clear the session
    return redirect('/')

#! READ(ONE)
@app.route('/user/show/<int:id>')
def show_one_users_recipes(id):
    data = {'id': id}
    return render_template("things.html", user = User.get_one_with_recipes(data))
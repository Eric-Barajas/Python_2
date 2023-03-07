from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    empty = request.form['empty']
    session['username'] = request.form['name']
    session['place'] = request.form['location']
    session['favorite'] = request.form['language']
    session['box'] = request.form['empty']
    return redirect("/show")	 

@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template('show.html')

# http://localhost:5000 - have this display a nice looking HTML form.  The form should be submitted to '/process'
# Save form data into session.
# http://localhost:5000/result - have this display a html with the information that was submitted by POST

# dont have any code under this
if __name__=="__main__":
    app.run(debug=True)    # Run the app in debug mode.


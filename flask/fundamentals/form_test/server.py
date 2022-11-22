from flask import Flask, render_template, request, redirect, session# added request and redirect
app = Flask(__name__)
app.secret_key = "any string you want" #encripts and jumbles up users post
# our index route will handle rendering our form

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session ['email'] = request.form['email']
    session ['name'] = request.form['name']
    return redirect('/')

# @app.route('/clear')
# def clear_session():

#     return redirect('/') 
# Never render a template on a POST request.
# Instead we will redirect to our index route.

if __name__ == "__main__":
    app.run(debug=True)



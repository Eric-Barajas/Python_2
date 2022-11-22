from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key="CHicken Boy"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def counter():
    if "num" not in session:
        session['num'] = random.randint(1,100) 		# random number between 1-100
    
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
# dont have any code under this
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


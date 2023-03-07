from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def eight_by_eight_():
    return render_template("index.html")


@app.route('/4')
def eight_by_four():
    return render_template("hello.html")

@app.route('/()x/(y)')
def x_by_y():
    return render_template("hello.html")

# http://localhost:5000/(x)/(y) - should display x by y checkerboard.  For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  Before you pass x or y to Jinja, please remember to convert it to integer first (so that you can use x or y in a for loop)

# dont have any code under this
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


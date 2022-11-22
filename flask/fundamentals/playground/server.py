from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_():
#     return render_template("index.html",phrase="hello", times=5)
@app.route('/play')
def play():
    return render_template("hello.html")

@app.route('/play/<int:num>')
def cat(num):
    return render_template("second.html", num=num)

@app.route('/play/<int:num>/<color>')
def change(color, num):
    return render_template("index.html", num=num, color=color)

# dont have any code under this
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


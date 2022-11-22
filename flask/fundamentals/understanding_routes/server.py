from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "hello World!"
# localhost:5000/ - have it say "Hello World!"
# localhost:5000/dojo - have it say "Dojo!"
@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def say(name):
    return f"Hi  {name}"
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"

@app.route("/repeat/<int:num>/<word>")
def repeat(num, word):
    return f"{word * num}"
# localhost:5000/repeat/35/hello - have it say "hello" 35 times

if __name__ == "__main__":
    app.run(debug = True)
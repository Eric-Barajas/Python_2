from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    print(request.form)
    if 'num' not in session:
        session['num'] = 1
    else:
        session['num'] += 1
    # num = request.form['num']
    # location = request.form['location']
    # session['Go_Up'] = request.form['num']
    # session['place'] = request.form['location']
    return render_template("index.html")

@app.route('/destroysession')
def destroy():
    session.clear()		# clears all keys
    # session.pop('key_name')		# clears a specific key
    return redirect("/")	 

# dont have any code under this
if __name__=="__main__":
    app.run(debug=True)    # Run the app in debug mode.


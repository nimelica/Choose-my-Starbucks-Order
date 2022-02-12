from flask import Flask, render_template, request, flash, g, session
import sqlite3, random

# Create instance of Flask by calling its class constructor
app = Flask(__name__)
app.secret_key = "12ev@0947!fbjs8$32jhbd_sjhAdhc%mhn_773gvsahG/HSI*IH_jbs"

# Main page
@app.route('/', methods=['GET'])
def index():
    flash("Hello! What's your name?")
    return render_template("index.html")

# When user enter her/his name
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    flash('Hi ' + str(request.form['name_input']).capitalize() + "! Time to choose your drink!")
    return render_template("index.html")


# run app
if __name__ == '__main__':
	app.run(debug=True)
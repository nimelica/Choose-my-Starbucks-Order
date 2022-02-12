from flask import Flask, render_template, request, flash
import requests, json
import sqlite3

# Create instance of Flask by calling its class constructor
app = Flask(__name__)
app.secret_key = "12ev@0947!fbjs8$32jhbd_sjhAdhc%mhn_773gvsahG/HSI*IH_jbs"

# Get data from the Mock API using GET HTTP method
# response data type will be byte
response = requests.get("https://mock-starbucs-api.herokuapp.com/drinks")

# Check if the request was successful
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')


# Convert bytes into a JSON list data
drinks_json = response.json()

# Create an empty database 
connection = sqlite3.connect('drinks_list.db')

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


# Do not forget to save (commit) and close the database connection
connection.commit()
connection.close()

# run app
if __name__ == '__main__':
	app.run(debug=True)
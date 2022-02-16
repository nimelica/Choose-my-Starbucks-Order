from flask import Flask, render_template, request, session, flash, g
import sqlite3, random

# Create instance of Flask by calling its class constructor
app = Flask(__name__)
app.secret_key = "12ev@0947!fBjs8AA#4$32jHbd_sjhAdhc%mhn_773gvPPahG/HSI*IH_jbs"
# Session data is stored at the top of the cookie
app.config['SESSION_COOKIE_NAME'] = "75jhbkdaCooKiebMONsteRRs!7)^&hbsh$4)"

# Main page
@app.route('/', methods=['GET'])
def index():
    flash("Click the button! Get your drink!")
    return render_template("index.html")


@app.route('/your_drink', methods=['GET', 'POST'])
def your_drink():
    item = get_db()
    return render_template("index.html", item=item)


# Managing database connection
# g is to manage resources during a request
# During a request, every call to get_db() will return the same connection, 
# and it will be closed automatically at the end of the request

# this function is connecting our database to our application
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('drinks_list.db')
        cursor = db.cursor()
        cursor.execute("select name from drinks")
        all_data = cursor.fetchall() # keeps all names in tuples
        all_names = [str(val[0]) for val in all_data] # hold names only

        random_drink = random.choice(all_names)
    return random_drink

# this function is terminating our database connection
# once we are done with using it
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# run app
if __name__ == '__main__':
	app.run(debug=True)
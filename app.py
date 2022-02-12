from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "12ev0947fbjs832jhbd_sjhAdhcmhn_773gvsahG/HSIIH_jbs"

@app.route('/', methods=['GET'])
def index():
    flash("Hello! What's your name?")
    return render_template("index.html")

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    flash('Hi ' + str(request.form['name_input']).capitalize() + "! time to choose your drink!")
    return render_template("index.html")


#run app
if __name__ == '__main__':
	app.run(debug=True)
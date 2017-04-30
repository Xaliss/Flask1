from flask import Flask, render_template, request, jsonify
import requests,json

app = Flask(__name__)


@app.route("/temp", methods =['GET'])
def temperature():
	#zipcode1 = request.form['zip']
	
	#tmp = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=b19377228ec064795f024f868c38403f')

	f = open("api_Mike_London.txt","r")
	tmp = f.read()
	pass
	k = json.loads(tmp)
	tt = float(k['main']["temp"])
	temp_f = (tt - 273.15)
	return(str(temp_f)+ "° C")

@app.route("/")
def index():
	return render_template("mapage.html")

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
 

@app.route('/shut', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Serveur en cours de fermeture...'


if __name__== "__main__":
	app.run(debug = True)
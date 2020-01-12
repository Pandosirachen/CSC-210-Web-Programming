"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
import json
from flask import Flask, render_template
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app



# https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.open_resource
with app.open_resource("users.json", 'r') as fin:
	u = json.load(fin)

@app.route("/users/<int:uid>")
def users(uid):
	dict = u[str(uid)]
	x = dict["friends"]
	x = list( map(str, x) )
	return render_template("hello.html", 
							user = dict,
							users = u,
							friends = x)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

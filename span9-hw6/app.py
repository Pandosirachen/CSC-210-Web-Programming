"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
import json
import datetime
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, DateField, validators
from wtforms.validators import DataRequired, Email, NumberRange

app = Flask(__name__)
app.config["SECRET_KEY"] = "oEHYBreJ2QSefBdUhD19PkxC"

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

sid=0

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
                            myuid = str(uid),
							friends = x)

@app.route("/update/<int:uid>", methods=["GET","POST"])
def rate(uid):
    flag=1
    dict = u[str(uid)]
    sid = uid
    fname,lname, email, dob= None, None, None, None
    form = RatingForm()

    if form.validate_on_submit():
        dict = u[str(uid)]
        x1 = dict["friends"]
        x1 = list(map(str,x1))
        dict["fname"] = form.fname.data
        form.fname.data = None

        dict["lname"] = form.lname.data
        form.lname.data = None
        
        dict["email"]= form.email.data
        form.email.data = None
        
        dict["dob"] = form.dob.data
        form.dob.data = None
        return render_template("hello.html",
                               user = dict,
							   users = u,
                               myuid = str(uid),
                               friends = x1)
    else:
        form.fname.data= str(u[str(uid)]["fname"])
        form.lname.data= str(u[str(uid)]["lname"])
        form.email.data= str(u[str(uid)]["email"])
        form.dob.data= datetime.datetime.strptime(str(u[str(uid)]["dob"]),"%Y-%m-%d")
    return render_template("rate.html", form=form)

class RatingForm(FlaskForm):
    fname = StringField("First Name")
    lname = StringField("Last Name")
    email = StringField("Email",validators=[DataRequired(), Email()])
    dob = DateField("Date Of Birth",validators=[DataRequired()])
    submit = SubmitField("Submit")

if __name__ == '__main__':
    app.run(debug=True, port=5000)

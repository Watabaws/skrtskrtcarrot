from flask import Flask, session, url_for, redirect, render_template, request

import os

#App instantiation
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def landing():
	print session;
	if "username" in session:
		return redirect("loggedin") #if logged in u go to logged in page otherwise you have to log in first
	return render_template("loginpage.html")

@app.route("/loggedin")
def pullup():
	print session;
	print "WE MADE IT \n\n"
	if "username" in session:
		return render_template("ushallpass.html", username = session["username"]) #if ur logged in this page is rendered
	else:
		return redirect("/")


#Where all the fun login stuff happens
@app.route("/loggit")
def logged(user = ""):
	#This part checks if your user+pw is correct.
	if user == "":
		username = request.args["user"].lower()
		password = request.args["passo"]
		print "BOUTTA CHECK THAT USERNAME \n\n"
		if username == "skrt":
			print "THE USERNAME HAS BEEN VALIDATED \n\n"
			if password == "Carrot":
				print "THE PASSWORD HAS BEEN VALIDATED \n\n"
				session["username"] = "skrt"
				print "Does we makes it?\n\n"
				return redirect("/loggedin") #actually logged in
			else:
				return redirect(url_for("u_messed_up", err="password")) #redirects to u_messed_up which tells you error of log in which happens to be wrong password
		else:
			return redirect(url_for("u_messed_up()", err="username")) #redirects to u_messed_up which tells you error of log in which happens to be wrong username

	#If you already have a username, it brings you here
	else:
		return render_template("ushallpass.html", username = session["username"])

@app.route("/wrong")
def u_messed_up():
    return render_template("errorpage.html", bad = request.args.get("err")) #returns the error you made >:(

if __name__ == "__main__":
    app.debug = True
    app.run()

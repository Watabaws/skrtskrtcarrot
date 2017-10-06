from flask import Flask, session, url_for, redirect

import os

#App instantiation
app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route("/")
def landing():
    if "username" in session:
        redirect("loggedin")
    return render_template("loginpage.html")
	
@app.route("/loggedin")
def pullup():
    if "username" in session:
        return render_template("ushallpass.html", username = session["username"]
    else:
        redirect("/")


#Where all the fun login stuff happens
@app.route("/loggit")
def logged(user = ""):
	#This part checks if your user+pw is correct.
	if user == "":
		username = request.args["user"].lower()
		password = request.args["passo"]
		if username == "skrt":
			if password == "Carrot":
				session["username"] = "wada"
				redirect("/loggedin")
			else:
				redirect(url_for("u_messed_up", err="password"))
		else:
			redirect(url_for("u_messed_up", err="username"))

	#If you already have a username, it brings you here
	else:
		return render_template("ushallpass.html", username = session["username"])

@app.route("/wrong")
def u_messed_up(rr):
    return render_template("errorpage.html", requests.args.get("err"))

if __name__ == "__main__":
    app.debug = True
    app.run()

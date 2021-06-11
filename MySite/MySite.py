#import flask
from flask import Flask, redirect, url_for,render_template
app = Flask(__name__)

#this will be the initial page you 
#see when you visit the domain
@app.route("/")
def home():
	return render_template("home.html")

@app.route("/projects/")
def projects():
	return render_template("projects.html")

@app.route("/contact/")
def contact():
	return render_template("contact.html")

@app.route("/about/")
def about():
	return render_template("about.html")

@app.route("/admin/")
def admin():
	return redirect(url_for("home"))

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

if __name__ == "__main__":
	app.run()
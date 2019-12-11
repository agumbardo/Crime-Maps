from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
	return render_template("home.html")

@app.route("/chicago")
def chicago():
	return render_template("chicago.html") 

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/vis1")
def vis1():
	return render_template("vis1.html")

@app.route("/vis2")
def vis2():
	return render_template("vis2.html")



if __name__ == "__main__":
	app.run()
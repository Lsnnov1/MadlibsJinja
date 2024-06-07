from flask import Flask, render_template , request
import stories

app = Flask(__name__)
app.config["SECRET_KEY"] = "Pure-secrecy"

@app.route("/madlib")
def show_form():
    return render_template("index.html")

@app.route("/story", methods=["POST"])
def show_story():
    location = request.form["location"]
    noun = request.form["noun"]
    verb = request.form["verb"]
    adj = request.form["adjective"]
    plu_noun = request.form["plural-noun"]
    return render_template("story.html", location=location, noun=noun, verb=verb, adj=adj, plu_noun=plu_noun)
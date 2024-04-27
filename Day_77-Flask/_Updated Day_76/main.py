from flask import Flask, redirect

app = Flask(__name__)

@app.route('/home')
def home():
    return redirect("/")

@app.route('/')
def index():
    f = open("template/index.html")
    page = f.read()
    f.close()
    return page

@app.route('/linktree')
def linktree():
    f = open("template/linktree.html")
    page = f.read()
    f.close()
    return page

@app.route('/portfolio')
def portfolio():
    myName = "Mike Lawson"
    f = open("template/portfolio.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{name}", myName)
    return page

app.run(host='0.0.0.0', port=81)
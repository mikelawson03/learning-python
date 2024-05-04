from flask import Flask, request

app = Flask(__name__)

@app.route("/") 
def index():
    f = open("template/index.html", "r")
    page = f.read()
    f.close()
    return page

@app.route("/submit", methods=["POST"])
def submit():
    cookware = request.form['cook']
    punisher = int(request.form['punisher'])
    org = request.form['org']
    score = 0
    message = ""

    if cookware == "kettle":
        score += 1
    if punisher > 0:
        score += 1
    if org == "blm":
        score += 1
    print(score)

    if score == 0:
        message = "You are definitely not a cop"
    elif score >0 and score <3:
        message = "You might not be a cop, but I bet your dad is"
    elif score == 3:
        message = "You are definitely a cop. Get out."

    print(message)

    f = open("template/results.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{message}", message)
    return page

app.run(host='0.0.0.0', port=81)


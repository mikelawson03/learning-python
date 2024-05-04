from flask import Flask, render_template, request, redirect

app = Flask(__name__)

theme = "default"

@app.route("/")
def index():
    
    name ="Mike Lawson"
    return render_template("index.html", name = name, theme = theme)

@app.route("/entry1")
def entry1():
    title = "First Entry"
    date = "January 1, 1999"
    content = """<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>"""
    return render_template("blog-template.html", title = title, date = date, content = content, theme = theme)

@app.route("/entry2")
def entry2():
    title = "Second Entry"
    date = "December 31, 1999"
    content = """<p>We are probably going to die. God bless the machines.</p>"""
    return render_template("blog-template.html", title = title, date = date, content = content, theme = theme)

@app.route("/update-theme", methods=['POST'])
def updateTheme():
    referrerURL = request.referrer
    global theme 
    theme = request.form['theme']
    return redirect(referrerURL)

app.run(host='0.0.0.0', port=81)
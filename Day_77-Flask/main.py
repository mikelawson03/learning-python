from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
    f = open("template/index.html", "r")
    page = f.read()
    page = page.replace("{name}", "Mike Lawson")
    f.close()
    return page

@app.route("/entry1")
def entry1():
    f = open("template/blog-template.html", "r")
    page = f.read()
    f.close()

    page = page.replace("{title}", "First Entry")
    page = page.replace("{date}", "January 1, 1999")
    page = page.replace("{content}", """<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>""")
    return page

@app.route("/entry2")
def entry2():
    f = open("template/blog-template.html", "r")
    page = f.read()
    f.close()

    page = page.replace("{title}", "Second Entry")
    page = page.replace("{date}", "December 31, 1999")
    page = page.replace("{content}", """We are probably going to die. God bless the machines.""")
    return page

app.run(host='0.0.0.0', port=81)
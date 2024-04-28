from flask import Flask

app = Flask(__name__)

reflections = {
    "78" : {
        "url" : "https://replit.com/@mikelawson03/Day78100Days",
        "description" : "Fought stupid favicon errors that weren't actually the real issue (the real issue was forgetting to put 'page =' before page.replace)"
    },
    "77" : {
        "url" : "https://replit.com/@mikelawson03/Day-77-Flask-Templates",
        "description" : "Use templates to display HTML pages"
    }
}

@app.route('/<pageNumber>')
def index(pageNumber):
    if pageNumber in reflections:
        f = open("template/day-template.html", "r")
        page = f.read()
        f.close()
        page = page.replace('{dayNumber}', pageNumber)
        page = page.replace('{url}', reflections[pageNumber]["url"])
        page = page.replace('{description}', reflections[pageNumber]["description"])
        return page
    else:
        return "This page does not exist"
    
@app.route('/')
def home():
    entries = ""
    for x in reflections:
        entries += f"""<p><a href="/{x}">Day {x}</a></p>"""
    f = open("template/index.html", "r")
    page = f.read()
    f.close()
    page = page.replace('{entries}', entries)
    return page

app.run(host='0.0.0.0', port=81)
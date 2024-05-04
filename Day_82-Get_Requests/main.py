from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    message = ''
    if request.args:
        lang = request.args['lang'].lower()
        if lang == 'es':
            message = '¡Hola! Bienvenido a nuestro sitio web.'
        elif lang == 'de':
            message = 'Hallo! Willkommen auf unserer Website.'
        elif lang == 'fr':
            message = 'Bonjour! Bienvenue sur notre site Web.'
        else:
            message = 'Hello! Welcome to our website.'
    else:
        message = 'Hello! Welcome to our website.'
    f = open("template/index.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{message}", message)
    return page





app.run(host='0.0.0.0', port='81')
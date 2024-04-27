from flask import Flask

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
    page = """<!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width">
            <title>Mike Lawson</title>
            <link href="static/lt-style.css" rel="stylesheet" type="text/css" />
        </head>
        <body>
            <h1 class="index-title">Mike Lawson</h1>
            <h2><a href="/linktree">Linktree</a></h2>
            <h2><a href="/portfolio">Portfolio</a></h2>
        </body>
    </html>
    """
    return page

@app.route('/linktree')
def linktree():
    page = f"""
    <!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Mike Lawson's Linktree</title>
  <link href="static/lt-style.css" rel="stylesheet" type="text/css" />
</head>

<body>
<img src = "static/images/headshot.jpg">
  <h1>Mike Lawson</h1>
  <h2>Socials</h2>
  <ul>
    <li>
      <a href="https://twitter.com/tacotime81">Twitter</a>
    </li>
    <li>
      <a href="https://www.linkedin.com/in/micheallawson1/">LinkedIn</a>
    </li>
    <li>
      <a href="https://github.com/mikelawson03">GitHub</a>
    </li>
    
  </ul>
  <h2>Projects</h2>
  <ul>
    <li>
      <a href="https://mikelawson03.github.io/stitch-calc/">Stitch Calculator</a>
    </li>
    <li>
      <a href="https://dnd-random-monster-gen.onrender.com/">D&D Monster Generator</a>
    </li>
  </ul>  
</body>
</html>
"""
    return page

@app.route('/portfolio')
def portfolio():
    page = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="static/pf-style.css" rel="stylesheet" type="text/css">
    <title>Mike Lawson's Portfolio</title>
</head>
<body>
  <h1>Mike Lawson - Portfolio</h1>
  
  <h2>Day 27: Character Creator</h2>
  <p>Allows user to enter a name and select a character class. Generates HP and ability scores for chosen class. Uses base D&D classes</p>
  <p>
    <a href="https://replit.com/@mikelawson03/Day-27-100-Days-of-Python-Character-Creator">
      <img src="static/images/day_27.png">
    </a>
  </p>
  
  <h2>Day 44: Bingo Card</h2>
  <p>Generates Bingo card, asks for user to input selected number, checks number against card, and changes matches to Xs. Once all numbers are Xs, it counts as a win</p>
  <p>
    <a href="https://replit.com/@mikelawson03/Day-44-100-Days-of-Python-Bingo-Card-v2">
      <img src="static/images/bingo.png">
    </a>
  </p>
  
  <h2>Day 46: Beast Dictionary</h2>
  <p>Creates a definitely not copyright-infringing dictionary of multiple beasts based on user input</p>
  <p>
    <a href="https://replit.com/@mikelawson03/Day-46-100-Days-of-Python-2D-Beast-Dictionary">
      <img src="static/images/day46.png">
    </a>
  </p>
  
  <h2>Day 65: Character Builder</h2>
  <p>Uses Python classes to generate characters for game. No user input at this time.</p>
  <p>
    <a href="https://replit.com/@mikelawson03/Day-65-100-Days-of-Python-Character-Builder">
      <img src="static/images/day65.png">
    </a>
  </p>
  
  <h2>Day 68: Guess Who</h2>
  <p>Not really guess who, but a program that lets you input a person's name to display an image of them.</p>
  <p>
    <a href="https://replit.com/@mikelawson03/Day-68-100-Days-Tkinter-Hide-and-Remove">
      <img src="static/images/day67.png">
    </a>
  </p>
  
</body>
</html>
"""
    return page

app.run(host='0.0.0.0', port=81)
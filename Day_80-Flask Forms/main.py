from flask import Flask, request

app = Flask(__name__)

logins = {
  "mike" : "test",
  "mike1" : "test1",
  "mike2" : "test2"
}


@app.route("/login", methods=["POST"])
def login():
  page = ""
  form = request.form
  loginUser = form["username"]
  loginPW = form["password"]
#   if loginUser == "mike":
#     return "Good"
  if loginUser in logins:
    if loginPW == logins[loginUser]:
      page = "Login successful"
    else:
      page = "Unrecognized Username"
  else:
#   except:
    page = "Incorrect password"
  return page

@app.route('/')
def index():
  page = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>replit</title>
    <link href="style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
    <form action="/login" method="post">
        
            <p>Username: <input type="text" name="username" required> </p>
            <p>Password: <input type="password" name="password" required> </p>
            <button type="submit">Login</button>
        
    </form>

    </body>

    </html>
    """
  return page
  
app.run(host='0.0.0.0', port=81)
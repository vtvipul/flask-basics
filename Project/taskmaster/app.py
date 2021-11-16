# Importing Flask from flask module
from flask import Flask, render_template, url_for

# initializing a flask application
app = Flask(__name__)

# dictionary to keep track of all templates
templates = dict()

templates["helloworld"] = "helloworld.html"
templates["mainpage"] = "mainpage.html"

# We need to route the user to somepage so that the application 
# doesn't give any error 404 when immediately accessed by an user
@app.route("/")
def hello_world():
    # code to check what url_for function generates
    url=url_for('static', filename='css/mainpage.css')
    return render_template(templates["helloworld"], url=url)


if __name__ == "__main__":
    app.run(debug=True)
    
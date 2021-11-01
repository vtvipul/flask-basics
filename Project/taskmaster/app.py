# Importing Flask from flask module
from flask import Flask

# initializing a flask application
app = Flask("taskmaster")

# We need to route the user to somepage so that the application 
# doesn't give any error 404 when immediately accessed by an user
@app.route("/")
def hello_world():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)
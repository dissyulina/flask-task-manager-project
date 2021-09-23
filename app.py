import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__) # create an instance of Flask, stored in a variable called app


@app.route("/")
def hello():
    return "Hello world"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) # make sure to set this to False prior to submission



from flask import Flask, request, jsonify


app = Flask(__name__, static_url_path="", static_folder="staticpages")

@app.route("/")
def index():
    return "<h1>AGHHHHHHHH</h1>"

@app.route("/inquery")
def inquery():
    name = request.args["name"]
    # return name 
    return request.args

@app.route("/inbody", methods = ["POST"])
def inbody():
    name = request.json["name"]
    age = request.json["age"]
    return request.json

if __name__ == "__main__":
    app.run(debug=True)

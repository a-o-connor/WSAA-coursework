from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path="", static_folder="staticpages")

@app.route("/")
def index():
    return "<h1>AGHHHHHHHH</h1>"

@app.route("/users", methods = ["GET"])
def users_get_route():
    return "GET the users"

@app.route("/users", methods = ["POST"])
def users_post_route():
    return "POST the users"

@app.route("/users", methods = ["PUT"])
def users_put_route():
    return "PUT the users"

@app.route("/users", methods = ["DELETE"])
def users_delete_route():
    return "DELETE the users"

@app.route("/users/<username>", methods=["GET"])
def username_route(username):
    return f"Hello {username}"

@app.route("/users/<int:id>", methods=["GET"])
def userid_route(id):
    return f"Your ID is {id}"

@app.route("/inquery")
def inquery():
    return request.args

@app.route("/inquery_post", methods = ["POST"])
def inquery_post():
    return request.args

@app.route("/inbody", methods = ["POST"])
def inbody():
    return request.json

if __name__ == "__main__":
    app.run(debug=True)
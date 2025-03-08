from flask import Flask


app = Flask(__name__, static_url_path="", static_folder="staticpages")

@app.route("/")
def index():
    return "<h1>AGHHHHHHHH</h1>"

@app.route("/users")
def users_route():
    return "Put a function here that returns the users?"

@app.route("/users/<username>", methods=["GET"])
def username_route(username):
    return f"Hello {username}"


@app.route("/users/<int:id>", methods=["GET"])
def userid_route(id):
    return f"Your ID is {id}"

@app.route("/users", methods=["POST"])
def user_post():
    return "Create a new user"

@app.route("/users", methods=["PUT"])
def user_put():
    return "Updoot user"


if __name__ == "__main__":
    app.run(debug=True)
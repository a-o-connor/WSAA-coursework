from flask import Flask, request, jsonify


app = Flask(__name__, static_url_path="", static_folder="staticpages")

@app.route("/")
def index():
    return "<h1>AGHHHHHHHH</h1>"

@app.route("/books", methods = ["GET"])
def getall():
    return "get all books"

@app.route("/books/<int:id>", methods = ["GET"])
def getbookbyid(id):
    return f"get book by id: {id}"

@app.route("/books", methods = ["POST"])
def createnewbook():
    json_book = request.json
    return f"create a new book {json_book}"

@app.route("/books/<int:id>", methods = ["PUT"])
def updateabook(id):
    update_book_with_json = request.json
    return f"update book {id} with {update_book_with_json}"

@app.route("/books/<int:id>", methods = ["DELETE"])
def deleteabook(id):
    return f"delete book {id}"

if __name__ == "__main__":
    app.run(debug=True)

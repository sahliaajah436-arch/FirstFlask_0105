from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    nama = None
    if request.method == "POST":
        nama = request.form.get("nama", "").strip()
    return render_template("index.html", nama=nama)

@app.route("/hello-world")
def hello_world():
    return "<p>Hello, World!</p><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYXj7sgzacSKFTO7Qnn2-l5neHy2B105An8O6flkGmjx6Gb3rUqb1WARCC&s=10.jpg'>"

@app.route("/home")
def home():
    return "Home page"

@app.route("/about")
def about():
    return "About us"

@app.route("/user/<name>")
def profile(name):
    return f"Hello, {name}!"

@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post #{post_id}"

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    nama = None
    if request.method == "POST":
        # parsing parameter dari form (method POST)
        nama = request.form.get("nama", "").strip()
    return render_template("index.html", nama=nama)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    context = {
        "switch1" : "active"
    }
    return render_template("index.html", **context)
@app.route("/about/")
def info():
    contex = {
        "switch2": "active"
    }
    return render_template("about.html", **contex)


if __name__ == "__main__":
    app.run()
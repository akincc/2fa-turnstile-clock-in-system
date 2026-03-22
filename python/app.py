from flask import Flask, render_template
from db import read_logs

app = Flask(__name__, template_folder="../docs")


@app.route("/")
def index():
    logs = read_logs()
    return render_template("index.html", logs=logs)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask

from utils import rupiah

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hi..</h1>"

@app.route("/to_rupiah/<int:amount>")
def to_rupiah(amount):
    return rupiah(amount)

if __name__ == "__main__":
    app.run(debug=True)
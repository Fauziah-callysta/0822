from flask import Flask
from utils import rupiah, slugify  # 1. Tambahkan import slugify di sini

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hi..</h1>"


# 2. Tambahkan route /slug/ di bawah ini
@app.route("/slug/<teks>")
def slug(teks):
    return slugify(teks)


@app.route("/to_rupiah/<int:amount>")
def to_rupiah(amount):
    return rupiah(amount)


if __name__ == "__main__":
    app.run(debug=True)

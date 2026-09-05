from deploy_webhook import deploy_bp
from flask import Flask
from utils import rupiah, slugify

app = Flask(__name__)
app.register_blueprint(deploy_bp)  # Daftarkan blueprint di sini


@app.route("/")
def index():
    return "<h1>Hi..</h1>"


@app.route("/slug/<teks>")
def slug(teks):
    return slugify(teks)


@app.route("/to_rupiah/<int:amount>")
def to_rupiah(amount):
    return rupiah(amount)


if __name__ == "__main__":
    app.run(debug=True)

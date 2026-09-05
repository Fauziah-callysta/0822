import hashlib
import hmac
import os
import subprocess
import requests
from flask import Blueprint, abort, request

deploy_bp = Blueprint("deploy_bp", __name__)

WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "")
PA_USERNAME = os.environ.get("PA_USERNAME", "")
PA_API_TOKEN = os.environ.get("PA_API_TOKEN", "")
PA_DOMAIN = os.environ.get("PA_DOMAIN", "")
PA_PYTHON_VERSION = os.environ.get("PA_PYTHON_VERSION", "3.12")
PROJECT_PATH = "/home/Callysta/0822"
UV_BIN = "/home/Callysta/.local/bin/uv"


def verify_signature(payload_body, signature_header):
    if not signature_header:
        return False
    hash_object = hmac.new(
        WEBHOOK_SECRET.encode("utf-8"), msg=payload_body, digestmod=hashlib.sha256
    )
    expected_signature = "sha256=" + hash_object.hexdigest()
    return hmac.compare_digest(expected_signature, signature_header)


@deploy_bp.route("/deploy-webhook", methods=["POST"])
def deploy_webhook():
    signature = request.headers.get("X-Hub-Signature-256")
    if not verify_signature(request.data, signature):
        abort(403)

    # 1. Pull kode terbaru dari GitHub
    subprocess.run(["git", "pull", "origin", "main"], cwd=PROJECT_PATH, check=True)

    # 2. Sync dependency dengan uv
    subprocess.run(
        [UV_BIN, "sync", "--no-dev", "--python", PA_PYTHON_VERSION],
        cwd=PROJECT_PATH,
        check=True,
    )

    # 3. Reload web app otomatis lewat API PythonAnywhere
    reload_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/webapps/{PA_DOMAIN}/reload/"
    resp = requests.post(
        reload_url, headers={"Authorization": f"Token {PA_API_TOKEN}"}
    )
    return {"status": "deployed", "reload_status": resp.status_code}, 200

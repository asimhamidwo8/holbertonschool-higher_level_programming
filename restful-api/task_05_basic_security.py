#!/usr/bin/env python3
"""
task_05_basic_security.py (no external deps)

Self-contained authentication example without external JWT libs.
Implements Basic Auth and a simple HMAC-signed token scheme (Bearer tokens).
"""
from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import base64
import hmac
import hashlib
import time

app = Flask(__name__)

# Secret for token HMAC (development only)
SECRET_KEY = b"super-secret-token-key"
TOKEN_EXP_SECONDS = 3600

# In-memory users
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"},
}


def make_token(username: str, role: str, exp_seconds: int = TOKEN_EXP_SECONDS) -> str:
    exp = int(time.time()) + exp_seconds
    payload = f"{username}:{role}:{exp}"
    sig = hmac.new(SECRET_KEY, payload.encode("utf-8"), hashlib.sha256).digest()
    token_bytes = payload.encode("utf-8") + b":" + base64.urlsafe_b64encode(sig)
    return base64.urlsafe_b64encode(token_bytes).decode("utf-8")


def verify_token(token: str):
    try:
        decoded = base64.urlsafe_b64decode(token.encode("utf-8"))
        # payload: username:role:exp
        payload_sig_split = decoded.rsplit(b":", 1)
        if len(payload_sig_split) != 2:
            return None, "Invalid token format"
        payload_bytes, sig_b64 = payload_sig_split
        try:
            sig = base64.urlsafe_b64decode(sig_b64)
        except Exception:
            return None, "Invalid signature encoding"
        payload = payload_bytes.decode("utf-8")
        parts = payload.split(":", 2)
        if len(parts) != 3:
            return None, "Invalid payload"
        username, role, exp_s = parts
        exp = int(exp_s)
        # recompute signature
        expected_sig = hmac.new(SECRET_KEY, payload_bytes, hashlib.sha256).digest()
        if not hmac.compare_digest(expected_sig, sig):
            return None, "Invalid signature"
        if int(time.time()) > exp:
            return None, "Token has expired"
        return {"username": username, "role": role, "exp": exp}, None
    except Exception:
        return None, "Invalid token"


def unauthorized_basic():
    resp = make_response("Unauthorized", 401)
    resp.headers["WWW-Authenticate"] = 'Basic realm="Login Required"'
    return resp


@app.route("/basic-protected", methods=["GET"])
def basic_protected():
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Basic "):
        return unauthorized_basic()
    try:
        b64 = auth.split(None, 1)[1]
        decoded = base64.b64decode(b64).decode("utf-8")
        username, password = decoded.split(":", 1)
    except Exception:
        return unauthorized_basic()
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return unauthorized_basic()
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 400
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad credentials"}), 401
    token = make_token(username, user["role"])
    return jsonify({"access_token": token}), 200


def bearer_auth_required(func):
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization")
        if not auth or not auth.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid token"}), 401
        token = auth.split(None, 1)[1]
        payload, err = verify_token(token)
        if err is not None:
            return jsonify({"error": "Missing or invalid token"}), 401
        # attach payload to request context for handlers
        request._token_payload = payload
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper


@app.route("/jwt-protected", methods=["GET"])
@bearer_auth_required
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@bearer_auth_required
def admin_only():
    payload = getattr(request, "_token_payload", None)
    if not payload:
        return jsonify({"error": "Missing or invalid token"}), 401
    if payload.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

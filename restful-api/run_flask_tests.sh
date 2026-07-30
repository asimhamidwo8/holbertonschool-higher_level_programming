#!/usr/bin/env bash

# Assumes current dir is restful-api and server already started in background

echo "--- GET / ---"
curl -sS -i http://127.0.0.1:5000/

echo

echo "--- GET /data ---"
curl -sS -i http://127.0.0.1:5000/data

echo

echo "--- GET /status ---"
curl -sS -i http://127.0.0.1:5000/status

echo

echo "--- GET /users/alice (expected 404) ---"
curl -sS -i http://127.0.0.1:5000/users/alice

echo

echo "--- POST /add_user (valid) ---"
curl -sS -i -H "Content-Type: application/json" -d '{"username":"alice","name":"Alice","age":25,"city":"SF"}' http://127.0.0.1:5000/add_user

echo

echo "--- GET /data (after add) ---"
curl -sS -i http://127.0.0.1:5000/data

echo

echo "--- GET /users/alice (after add) ---"
curl -sS -i http://127.0.0.1:5000/users/alice

echo

echo "--- POST /add_user (duplicate) ---"
curl -sS -i -H "Content-Type: application/json" -d '{"username":"alice","name":"Alice2"}' http://127.0.0.1:5000/add_user

echo

echo "--- POST /add_user (invalid JSON) ---"
curl -sS -i -H "Content-Type: application/json" -d '{bad json' http://127.0.0.1:5000/add_user

echo

# show log tail
sleep 0.2
pkill -f task_04_flask.py || true

echo "--- flask log excerpt ---"
tail -n +1 /tmp/flask_app.log | sed -n '1,200p' || true

#!/usr/bin/env bash

cd "$(dirname "$0")"

# start server
nohup python3 task_05_basic_security.py >/tmp/task05_server.log 2>&1 &
PID=$!
sleep 0.6

echo "--- GET /basic-protected (no auth) ---"
curl -sS -i http://127.0.0.1:5002/basic-protected || true

echo

echo "--- GET /basic-protected (with basic auth user1) ---"
# basic auth: user1:password
creds=$(printf "user1:password" | base64)
curl -sS -i -H "Authorization: Basic $creds" http://127.0.0.1:5002/basic-protected || true

echo

echo "--- POST /login (user1) ---"
curl -sS -i -H "Content-Type: application/json" -d '{"username":"user1","password":"password"}' http://127.0.0.1:5002/login || true

echo

echo "--- POST /login (admin1) ---"
curl -sS -i -H "Content-Type: application/json" -d '{"username":"admin1","password":"password"}' http://127.0.0.1:5002/login || true

echo

echo "--- GET /jwt-protected (no token) ---"
curl -sS -i http://127.0.0.1:5002/jwt-protected || true

echo

echo "--- GET /admin-only (user token) ---"
# get user token
USER_TOKEN=$(curl -s -H "Content-Type: application/json" -d '{"username":"user1","password":"password"}' http://127.0.0.1:5002/login | python3 -c "import sys, json; print(json.load(sys.stdin).get('access_token',''))")
if [ -n "$USER_TOKEN" ]; then
  curl -sS -i -H "Authorization: Bearer $USER_TOKEN" http://127.0.0.1:5002/admin-only || true
else
  echo "no user token"
fi

echo

echo "--- GET /admin-only (admin token) ---"
ADMIN_TOKEN=$(curl -s -H "Content-Type: application/json" -d '{"username":"admin1","password":"password"}' http://127.0.0.1:5002/login | python3 -c "import sys, json; print(json.load(sys.stdin).get('access_token',''))")
if [ -n "$ADMIN_TOKEN" ]; then
  curl -sS -i -H "Authorization: Bearer $ADMIN_TOKEN" http://127.0.0.1:5002/admin-only || true
else
  echo "no admin token"
fi


echo

echo "--- server log (tail) ---"
tail -n +1 /tmp/task05_server.log | sed -n '1,200p' || true

kill $PID || true

#!/usr/bin/env python3
"""Javier Duran MiniProject3"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import make_response
from flask import render_template
from flask import url_for

import json

app= Flask(__name__)

herodata= [{
    "name": "Sub-Mariner",
    "realName": "Namor",
    "since": 1939,
    "powers": [
        "powers of all sea creatures",
        "generate power from eel",
        "sense presence of Sue Storm",
        "super human strength & agility"
              ]
             }]

@app.route("/")
def index():
    return jsonify(herodata)

@app.route("/setcookie", methods=["GET","POST"])
def setcookie():
    if request.method == 'POST':
        data = request.json
        if data:
           data= json.loads(data)
           name = data["name"]
           realName = data["realName"]
           since = data["since"]
           powers = data["powers"]
           herodata.append({"name":name,"realName":realName,"since":since,"powers":powers})
        
        hero = data["name"]
        print(hero)
        resp = make_response(render_template("readcookie.html"))

        resp.set_cookie("heroname", hero)

    return resp

    if request.method == "GET":
        return redirect(url_for("index"))

@app.route("/getcookie")
def getcookie():
    heroName = request.cookies.get("heroname")

    return f'<h1>Welcome {heroName}</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

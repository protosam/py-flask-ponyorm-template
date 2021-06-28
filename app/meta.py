#!/usr/bin/env python3
from __main__ import app
from flask import render_template
from pony.orm.core import desc
import json

@app.server.route("/")
def hello_world():
    return render_template('index.html.j2', vars={ "username": "world" }) + "\n"

# This is an example of using a decorator to gatekeep access to paths.
# Test with these commands:
#   curl -iL http://localhost:5000/auth-example/
#   curl -iL -H 'username: abc' http://localhost:5000/auth-example/
from .shared.auth import login_required
@app.server.route("/auth-example/")
@login_required
def hello_world_auth(username):
    return render_template('index.html.j2', vars={ "username": username }) + "\n"

# Quick database crud test
# curl -iL http://localhost:5000/items/create/bag-of-holding/holds-a-ton-of-stuff/
# curl -iL http://localhost:5000/items/get/bag-of-holding/
# curl -iL http://localhost:5000/items/update/bag-of-holding/holds-a-lot-of-stuff/
# curl -iL http://localhost:5000/items/get/bag-of-holding/
# curl -iL http://localhost:5000/items/delete/bag-of-holding/
# curl -iL http://localhost:5000/items/get/bag-of-holding/
from pony import orm
from models.items import Item

@app.server.route("/items/create/<item_name>/<description>/", methods=['GET'])
@orm.db_session
def item_create(item_name, description):
    i = Item.get(name=item_name)
    if i != None:
        return 'item already exists - ' + item_name + "\n"

    i = Item(name=item_name, desc=description)
    return "created item - " + item_name + " - " + description + "\n"

@app.server.route("/items/get/<item_name>/", methods=['GET'])
@orm.db_session
def item_get(item_name):
    i = Item.get(name=item_name)
    if i == None:
        return 'No such item - ' + item_name + "\n"
    return "item info: - " + json.dumps(i.to_dict()) + "\n"

@app.server.route("/items/delete/<item_name>/", methods=['GET'])
@orm.db_session
def item_delete(item_name):
    i = Item.get(name=item_name)
    if i == None:
        return 'No such item - ' + item_name + "\n"
    i.delete()
    return 'Item deleted - ' + item_name + "\n"


@app.server.route("/items/update/<item_name>/<description>/", methods=['GET'])
@orm.db_session
def item_update(item_name, description):
    i = Item.get(name=item_name)
    if i == None:
        return 'No such item - ' + item_name + "\n"
    i.desc = description
    return "item updated: - " + json.dumps(i.to_dict()) + "\n"
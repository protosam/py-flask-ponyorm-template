#!/usr/bin/env python3
from .shared.base import db
from pony import orm

class Item(db.Entity):
    name    = orm.PrimaryKey(str)
    desc    = orm.Required(str)


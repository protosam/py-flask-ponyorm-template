#!/usr/bin/env python3
from .shared.base import db
from pony import orm

class User(db.Entity):
    name    = orm.Required(str)
    age     = orm.Required(int)
    cars    = orm.Set('Car')


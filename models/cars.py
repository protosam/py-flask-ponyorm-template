#!/usr/bin/env python3
from .shared.base import db
from pony import orm
from .users import User

class Car(db.Entity):
    make    = orm.Required(str)
    model   = orm.Required(str)
    owner   = orm.Required(User)

#!/usr/bin/env python3
import os
from os.path import join
from pony import orm
from .base import db
orm.set_sql_debug(True)

if os.environ['FLASK_ENV'] == 'production':
    pass # TODO: Implement
    # PostgreSQL
    #db.bind(provider='postgres', user='', password='', host='', database='')
    # MySQL
    #db.bind(provider='mysql', host='', user='', passwd='', db='')
    # Oracle
    #db.bind(provider='oracle', user='', password='', dsn='')
    # CockroachDB
    #db.bind(provider='cockroach', user='', password='', host='', database='', )
else:
    # SQLite (don't use :memory:, there be dargons)
    sqlite_file = join(os.getcwd(), "database.sqlite")
    if os.path.exists(sqlite_file):
     os.remove(sqlite_file)

    db.bind(provider='sqlite', filename=sqlite_file, create_db=True)

db.generate_mapping(create_tables=True)
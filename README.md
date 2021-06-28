# Python MVC Template
This is an amalgamation of combining Flask and Pony ORM to achieve something akin to an MVC pattern. It's just a boilerplate to get web based python projects off the ground.

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [PonyORM](https://docs.ponyorm.org/)
* [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/)

Clone this repo and be sure to edit `models/shared/loader.py`. Later this will be updated to work based on environment variables. Also load you passwords from environment variables, don't store them in code.

Some database usage examples are included in `app/meta.py`.

New `.py` files can just be dumped in `app/` and `models/` and they will be automatically reloaded.

# Lessons Learned
Don't use `:memory:` when using SQLite. It's just going to lead to a bad time due to how modules are loaded and memory is referenced in python. Due to this I also have a sneaking suspicion that it might also be capable of opening a SQLite database file twice, so SQLite is reserved for local testing only and it shouldn't be trusted. Remote databases should be fine, the statefulness is handled remotely.

Pony is pretty cool, but for the reasons it is awesome it also sucks too. I would prefer to have a `.save()` function.

In Pony, [rollback()](https://docs.ponyorm.org/api_reference.html#rollback) is a friend you want to get to know.

The auto reload feature that happens in development does not see new files being created, it only monitors existing files.

# Running in Production
It's going to throw a warning to use `flask run` instead. Flask, stop trying to dictate my life, you are a library and you will act like one.
```text
# FLASK_ENV=development python3 main.py
```

# Running in Development
It's very nice how it auto-reloads. Something to note is that it will reload upon first starting, so don't worry about the duplicate output you see when debugging.
```text
# FLASK_ENV=development python3 main.py
```
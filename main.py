#!/usr/bin/env python3
import models
import app
from app import *

app.server.run("0.0.0.0", 5000)
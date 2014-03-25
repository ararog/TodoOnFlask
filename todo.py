# -*- coding: utf-8 -*-
"""
Todo
~~~~~~

A simple todo application.

:copyright: (c) 2014 by Rogerio Araujo.
:license: BSD, see LICENSE for more details.
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create our little application :)
app = Flask(__name__)
app.config.from_pyfile('todo.cfg')
db = SQLAlchemy(app)

import views

if __name__ == '__main__':
    app.run()

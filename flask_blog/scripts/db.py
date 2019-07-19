# flask_blog/scrips/db.py

from flask_script import Command
from flask_blog import db


class InitDB(Command):
    "create databese"

    def run(self):
        db.create_all()

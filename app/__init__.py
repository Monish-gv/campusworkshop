"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq1p02qv2dcb92aubg-a.oregon-postgres.render.com",
        database="todo_3eir",
        user="root",
        password="5cYPfip03K9XrGM9eigdh81uFEv6ZBRv")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes

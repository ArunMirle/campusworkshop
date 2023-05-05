"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaagke7avj5o48sm22g-a.oregon-postgres.render.com",
        database="todo_z6kw",
        user="todo_z6kw_user",
        password="cK5f8OUPT3USyWGdyrviOAbAs46qup2U")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes

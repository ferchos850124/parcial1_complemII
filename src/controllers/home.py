from flask import render_template
from src import app

@app.route('/')
def index():
    return "Ingrese al Puerto: 5000/db"
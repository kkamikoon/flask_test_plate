from flask import Flask
from flask import (
    request,
    redirect
)

app = Flask(__name__)

from app import methods


@app.route("/")
def index():
    return "Index Page"

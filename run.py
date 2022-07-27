import os
os.environ['FLASK_ENV'] = 'development'
# from flask import Flask, render_template
# from flask_restx import Api
# from project.config import DevelopmentConfig
from project.config import config
from project.models import Genre
from project.server import create_app, db


app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
    }

if __name__ == '__main__':
    app.run(port=7777, debug=True)

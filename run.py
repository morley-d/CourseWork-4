import os
print(os.environ.get('FLASK_ENV'))

os.environ['FLASK_ENV'] = 'development'
from flask import Flask, render_template
from flask_restx import Api
from project.config import DevelopmentConfig
from project.config import config
from project.models import Genre
from project.server import create_app, db

api = Api(title="Flask Course Project 3", doc="/docs")


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/')
    def index():
        return render_template('index.html')

    db.init_app(app)
    api.init_app(app)

    return app


app = create_app()


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
    }

if __name__ == '__main__':
    app.run(port=25000, debug=True)
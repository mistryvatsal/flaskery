from application.jobs import test_job
from application import jobs
from flask import Flask
from flask_restx import Api
import os
from celery import Celery
from config import Config


def make_celery(app=None):
    app = app or create_app()
    celery_app = Celery(
        app.import_name,
        broker=Config.CELERY_BROKER_URL,
        backend=Config.RESULT_BACKEND
    )
    celery_app.conf.update(app.config)

    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app

# Application Factory 
def create_app():
    app = Flask(__name__)

    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)
    

    # Register blueprints
    register_blueprints(app)

    # Initialize flask extension objects
    # initialize_extensions(app)

    # Create Celery app
    celery_app = make_celery(app)

    # Configure logging
    # configure_logging(app)

    # Register error handlers
    # register_error_handlers(app)
    return app

def register_blueprints(app):
    from application.routes import init_routes
    api = Api(app, version='1.0', title='Flaskery API', description='A simple API')
    with app.app_context():
        init_routes(api)

def initialize_extensions(app):
    pass

def configure_logging(app):
    pass

def register_error_handlers(app):
    pass
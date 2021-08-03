#!/usr/bin/env python
import os

from flask_restx.marshalling import make
from application import make_celery, create_app

app = create_app()
app.app_context().push()

celery_app = make_celery(app)
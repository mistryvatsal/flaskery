import os
from application import create_app

app = create_app()
app.app_context().push()

from application import celery_app
from application import celery_app


@celery_app.task
def test_job():
    print("test_job")

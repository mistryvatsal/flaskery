from celery_worker import celery_app
import time

@celery_app.task
def test_job():
    print('test-job-start')
    time.sleep(5)
    print('test-job-end')
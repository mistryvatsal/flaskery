from flask_restx import Resource
from application.jobs.test_job import test_job
class TriggerJob(Resource):
    def get(self):
        print('Triggering Job')
        t = test_job.delay()
        print('Job Triggered Successfully')
        return {
            'message': 'job triggered sucessfully',
            'job_id': t.id
        }
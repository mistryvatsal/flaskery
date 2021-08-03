from flask_restx import Resource, reqparse
from celery.result import AsyncResult

class JobStatus(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('job_id', help = 'Job ID', type = str)

    def get(self):
        args = self.parser.parse_args()
        job_id = args['job_id']
        job = AsyncResult(job_id)

        return {
            'job_id': job_id,
            'job_status': job.status
            }
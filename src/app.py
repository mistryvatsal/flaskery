from flask import Flask
from flask_restx import Api, Resource, reqparse
from .tasks import test_job

app = Flask(__name__)
api = Api(app)

# Normal End Point
# Add these to one namespace -> analytics
class HelloWorld(Resource):
    def get(self):
        return {'message': 'hello world'}

# Job/Task Related End point
# Add these to other namespace -> celery
class TriggerJob(Resource):
    def get(self):
        print('Triggering Job')
        t = test_job.delay()
        print('Job Triggered Successfully')
        return {
            'message': 'Job Triggered Successfully',
            'job_id': t.id
        }

class GetJobStatus(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('job_id', type=str)

    def get(self):
        args = self.parser.parse_args()
        job_id = args['job_id']
        print('Checking Job Status')
        job = test_job.AsyncResult(job_id)
        print('Job Status: {}'.format(job.state))
        return {
            'job_id': job.id,
            'job_tatus' : job.state
        }
        
ns_analytics = api.namespace('analytics', description='Analytics Endpoints')
ns_celery = api.namespace('celery', description='Celery Endpoints')

ns_analytics.add_resource(HelloWorld, '/hello/')

ns_celery.add_resource(TriggerJob, '/trigger_job/')
ns_celery.add_resource(GetJobStatus, '/get_job_status/')

if __name__ == '__main__':
    app.run(debug=True)
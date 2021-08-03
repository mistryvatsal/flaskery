from application.resources.HelloWorld import HelloWorld
from application.resources.JobStatus import JobStatus
from application.resources.TriggerJob import TriggerJob

def init_routes(api):
    api.add_resource(HelloWorld, '/hello/')
    api.add_resource(JobStatus, '/get_job_status/')
    api.add_resource(TriggerJob, '/trigger_job/')
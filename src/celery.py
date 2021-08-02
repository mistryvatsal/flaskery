from celery import Celery

rbt_mq_user = 'guest'
rbt_mq_password = 'guest'
rbt_mq_host = 'localhost'
rbt_mq_port = 5672
rbt_mq_vhost = '/'

celery_app = Celery(
    'src', 
    broker = f'amqp://{rbt_mq_user}:{rbt_mq_password}@{rbt_mq_host}:{rbt_mq_port}/{rbt_mq_vhost}',
    backend = 'rpc://',  
    include=['src.tasks']
    )

if __name__ == '__main__':
    celery_app.start()
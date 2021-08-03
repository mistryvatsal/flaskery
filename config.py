class Config():
    APP_NAME = 'Flaskery'
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False

    rbt_mq_user = 'guest'
    rbt_mq_password = 'guest'
    rbt_mq_host = 'localhost'
    rbt_mq_port = 5672
    rbt_mq_vhost = '/'

    CELERY_BROKER_URL = f'amqp://{rbt_mq_user}:{rbt_mq_password}@{rbt_mq_host}:{rbt_mq_port}/{rbt_mq_vhost}'
    RESULT_BACKEND = 'rpc://'
    
class DevelopmentConfig(Config):
    DEBUG = True
    
class TestConfig(Config):
    pass

class ProductionConfig(Config):
    FLASK_ENV = 'production'
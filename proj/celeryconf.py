from kombu import Queue, Exchange
from kombu.common import Broadcast
from datetime import timedelta

BROKER_URL = 'amqp://'
BROKER_POOL_LIMIT = 10

CELERY_RESULT_BACKEND = 'amqp'
CELERY_RESULT_PERSISTANCE = True
CELERY_IMPORTS = ('proj.tasks',)

CELERY_ANNOTATIONS = {
    '*': {'rate_limit': '10/s'}
}

# CELERY_ENABLE_UTC = True
# CELERY_TIMEZONE = 'Europe/Kiev'
CELERY_TIMEZONE = 'UTC'
CELERY_TASK_SERIALIZER   = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT    = ['json']
CELERY_MESSAGE_COMPRESSION = 'gzip'
CELERYD_STATE_DB = 'celery_worker_state'

CELERY_ACKS_LATE = True
CELERYD_PREFETCH_MULTIPLIER = 1

CELERYD_POOL_RESTARTS = True

CELERY_CREATE_MISSING_QUEUES = False
CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = (
    Queue('default', exchange=Exchange('default', type='direct'), routing_key='default', delivery_mode=2),
    Queue('add',     exchange=Exchange('add',     type='direct'), routing_key='add',     delivery_mode=1),
    Queue('mul',     exchange=Exchange('mul',     type='direct'), routing_key='mul',     delivery_mode=2),
    Queue('xsum',    exchange=Exchange('xsum',    type='direct'), routing_key='xsum',    delivery_mode=1),
    Broadcast('broadcast_tasks'),
)
CELERY_DEFAULT_EXCHANGE      = 'default'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_ROUTING_KEY   = 'default'

CELERY_ROUTES = {
                    'app.task.add': {
                        'queue': 'add',
                        'routing_key': 'add'
                    },
                    'app.task.mul': {
                        'queue': 'mul',
                        'routing_key': 'mul'
                    },
                    'app.task.xsum': {
                        'queue': 'xsum',
                        'routing_key': 'xsum'
                    },
                },

CELERYBEAT_SCHEDULE = {
    'add_every_10_seconds': {
        'task': 'app.task.add',
        'schedule': timedelta(seconds=10),
        'args': (1, 123),
    },
}
CELERY_SEND_EVENTS = True
CELERY_SEND_TASK_SENT_EVENT = True

CELERY_TASK_PUBLISH_RETRY_POLICY = {
    'max_retries': 5,
    'interval_start': 0.5,
    'interval_step': 0.5,
    'interval_max': 0.5,
}

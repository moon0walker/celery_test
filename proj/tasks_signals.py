from json import dumps as json_dumps
from celery.signals import after_task_publish, before_task_publish, task_success, task_failure

from .logger import logger


@before_task_publish.connect
def before_task_sent_handler(sender=None, body=None, **kwargs):
    print(10*'=', 'before_task_publish', 10*'=')
    # print(json_dumps(body, indent=4))
    logger.info('before_task_sent_handlerfor task [{sender}] id [{body[id]}]'.format(sender=sender, body=body))


# @after_task_publish.connect(sender='app.task.mul')
@after_task_publish.connect
def after_task_sent_handler(sender=None, body=None, **kwargs):
    print(10*'=', 'after_task_publish', 10*'=')
    # print(json_dumps(body, indent=4))
    logger.info('after_task_publish for task [{sender}] id [{body[id]}]'.format(sender=sender, body=body))


@task_success.connect
def task_success_handler(sender=None, **kwargs):
    logger.info('sender =  {sender} | kwargs = {kwargs}'.format(sender=sender, kwargs=str(kwargs)))


@task_failure.connect
def task_failure_handler(sender=None, **kwargs):
    logger.error('sender =  {sender} | kwargs = {kwargs}'.format(sender=sender, kwargs=str(kwargs)))

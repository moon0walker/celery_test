from .celery import app
from .tasks_signals import *
from .workers_signals import *


@app.task(name='app.task.error_handler', bind=True)
def error_handler(self, uuid):
    result = self.app.AsyncResult(uuid)
    logger.error('Task {0} raised exception: {1!r}\n{2!r}'.format(uuid, result.result, result.traceback))


@app.task(name='app.task.get_prime')
def get_prime(x):
    multiples = []
    results = []
    for i in range(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in range(x*i, x+1, i):
                multiples.append(j)
    return results


@app.task(name='app.task.add', bind=True)
def add(self, x, y):
    import time
    time.sleep(10)
    return x+y


@app.task(name='app.task.mul')
def mul(x, y):
    return x*y


@app.task(name='app.task.xsum')
def xsum(numbers):
    return sum(numbers)

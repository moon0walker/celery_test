# from __future__ import absolute_import
from celery import Celery

app = Celery('proj')
app.config_from_object('proj.celeryconf')

if __name__ == '__main__':
    app.start()

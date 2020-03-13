from celery import Celery
from server import app
from celery.schedules import crontab

def base_configuration():
    application = app
    application.config['CELERY_BROKER_URL'] ='redis://localhost'
    application.config['imports']= ("services.celery_task")

    _celery = Celery(__name__, broker=application.config['CELERY_BROKER_URL'])
    _celery.conf.beat_schedule = {
        'cron-every-min-celery':{
            'task': 'services.celery_task.cron_min_scheduler',
            'schedule': crontab(),
            'args': (16, 16)
        },
        'cron-every-15-min-celery': {
            'task': 'services.celery_task.cron_scheduler',
            # Execute daily at midnight.
            # 'schedule': crontab(minute=0, hour=0),
            #  Executes every day at  11:30 pm.
            # 'schedule': crontab(hour=11, minute=30),
            # Execute every 5 minutes.
            'schedule': crontab(minute='*/15'),
            #Execute every minutes.
            # 'schedule': crontab(),
            'args': (16, 16)
        },
        "cron-every-hour-celery":{
            'task': 'services.celery_task.cron_hour_scheduler',
            'schedule':crontab(minute=0, hour='*'),
            'args': (16, 16)
        },
        "cron-every-mid-night":{
            'task': 'services.celery_task.cron_midnight_scheduler',
            'schedule': crontab(minute=0, hour=0),
            'args': (16, 16)
        }

    }
    _celery.conf.update(application.config)
    return _celery

_celery = base_configuration()

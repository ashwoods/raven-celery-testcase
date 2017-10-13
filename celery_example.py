import celery
from raven import Client
from raven.contrib.celery import register_signal, register_logger_signal

client = Client()

# Sentry
register_logger_signal(client)
register_signal(client)


# Exception
class MyCeleryException(Exception):
    pass


# Celery
celery_app = celery.Celery()
#celery_app.conf.broker_url = 'redis://localhost:32768/0'
celery_app.conf.broker_url = 'amqp://localhost:32774'


@celery_app.task(name='test')
def test():
    raise MyCeleryException("We are under attack!")


@celery_app.task(name='message')
def message():
    client.captureMessage("This is just a message!")

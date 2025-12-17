import os
import time
import random

from celery import Celery

from celery.schedules import crontab
from datetime import timedelta

from mailer import send_email_logic

app = Celery(
    'random_number',
    broker = os.getenv('CELERY_BROKER_URL'),
    backend = os.getenv('CELERY_BACKEND_URL')
)


@app.task
def mail_task(email_address):
    subject = "Buckethead"
    url = "https://www.youtube.com/watch?v=0kTATlcELzM&list=RDEhkEiHUG1QM&index=2"
    return send_email_logic(email_address, subject, url)
# def random_number(max_value=100):
#     time.sleep(5)
#     result = random.randint(0,max_value)

#     print(f"RESULT PROCESSED = {result}")
#     return result


# --- CELERY BEAT SCHEDULE ---
app.conf.beat_schedule = {
    'run-random-number-every-2-minutes': {
        'task': 'worker.mail_task',
        'schedule': timedelta(minutes=1), # Time in seconds if not using timedelta (60.0)
        'args': ("arghya07cse@gmail.com",)     # Arguments passed to the function as tuple
    },
}
app.conf.timezone = 'UTC'
from dashbash.worker import app_celery


@app_celery.task()
def add_together(a, b):
    return a + b
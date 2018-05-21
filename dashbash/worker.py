from celery import Celery
from dashbash.settings import Config

app_celery = Celery(__name__,
                    backend=Config.CELERY_RESULT_BACKEND,
                    broker=Config.CELERY_BROKER_URL)


def create_task_queue(app):
    app_celery.conf.update(app.config)

    class ContextTask(app_celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    app_celery.Task = ContextTask
    return None

# $ celery worker -A dashbash.tasks.user_tasks -l info

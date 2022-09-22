from __future__ import absolute_import, unicode_literals


def init_celery(app, celery):
    celery.conf['mongodb_backend_settings'] = {
        "options": {
            "authSource": "admin",
        },
    }

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery

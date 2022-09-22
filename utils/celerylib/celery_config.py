#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from config import settings
# CELERY
broker_url = "amqp://{user}:{password}@{host}:{port}/{vhost}".format(
    user=settings.RABBITMQ_USER,
    password=settings.RABBITMQ_PASSWORD,
    host=settings.RABBITMQ_HOST,
    port=settings.RABBITMQ_PORT,
    vhost=settings.RABBITMQ_V_HOST,
)
imports = ('utils.celerylib.tasks', )
result_backend = f"{settings.MONGO_URI}?authSource=admin"
timezone = os.getenv("CELERY_TIMEZONE", "Asia/Shanghai")
retry_delay = 30
max_retries = 5

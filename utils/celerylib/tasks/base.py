#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from pathlib import Path
from config import settings
from logging.handlers import TimedRotatingFileHandler
from utils.celerylib import celery, after_setup_logger


logger = logging.getLogger("celery")


@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    celery_log_dir = Path(settings.BASE_DIR, 'logs', 'celery')
    if not celery_log_dir.exists():
        celery_log_dir.mkdir(parents=True, exist_ok=True)
    logformat = logging.Formatter(
        "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(process)d][%(threadName)s] - %(message)s")
    handler = TimedRotatingFileHandler(
        Path(celery_log_dir, 'celery.log'),
        when="midnight",
        interval=1,
        backupCount=30,
        encoding='utf-8'
    )
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logformat)
    logger.addHandler(handler)


@celery.task(
    bind=True
)
def test_task(self):
    return ""

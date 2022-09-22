#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
from flask import Flask
from flask_pymongo import PyMongo
from config import settings
from pathlib import Path
from datetime import timedelta
from flask_jwt_extended import JWTManager
from app.routers import register_blueprints
from logging.handlers import TimedRotatingFileHandler
from utils.celerylib import celery
from utils.celerylib.celery_util import init_celery


def register_jwt(app: Flask):
    app.config["JWT_SECRET_KEY"] = settings.SECRET_KEY
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=48)
    jwt = JWTManager(app)
    app.jwt = jwt


def register_mongo(app: Flask):
    app.mongo = PyMongo(app, authSource="admin", serverSelectionTimeoutMS=10)


def init_logs(app):
    upload_file_dir = Path(settings.BASE_DIR, "upload_files")
    if not upload_file_dir.exists():
        upload_file_dir.mkdir(parents=True)

    flask_debug_log_dir = Path(settings.BASE_DIR, 'logs', 'flask', 'debug')
    if not flask_debug_log_dir.exists():
        flask_debug_log_dir.mkdir(parents=True, exist_ok=True)

    flask_error_log_dir = Path(settings.BASE_DIR, 'logs', 'flask', 'error')
    if not flask_error_log_dir.exists():
        flask_error_log_dir.mkdir(parents=True, exist_ok=True)

    app.config['UPLOAD_FOLDER_DIR'] = upload_file_dir
    app.config['LOG_FILE_FOLDER_DIR'] = str(Path(settings.BASE_DIR, 'logs'))

    logformat = logging.Formatter(
        "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(process)d][%(threadName)s] - %(message)s")
    logger = app.logger
    logger.handlers.clear()

    # time rotating handler
    # debug
    debug_rotating_handler = TimedRotatingFileHandler(
        Path(flask_debug_log_dir, 'flask.log'),
        when="midnight",
        interval=1,
        backupCount=settings.LOG_FILE_MAX,
        encoding='utf-8'
    )
    debug_rotating_handler.setFormatter(logformat)
    debug_rotating_handler.setLevel(logging.DEBUG)
    logger.addHandler(debug_rotating_handler)
    # error
    error_rotating_handler = TimedRotatingFileHandler(
        Path(flask_error_log_dir, 'flask.log'),
        when="midnight",
        interval=1,
        backupCount=settings.LOG_FILE_MAX,
        encoding='utf-8'
    )
    error_rotating_handler.setFormatter(logformat)
    error_rotating_handler.setLevel(logging.ERROR)
    logger.addHandler(error_rotating_handler)
    # stream handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logformat)
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)
    logger.setLevel(logging.DEBUG)

    gunicorn_error_logger = logging.getLogger('gunicorn.access')
    gunicorn_error_logger.handlers = logger.handlers
    gunicorn_error_logger.setLevel(logging.DEBUG)


def create_app():
    app = Flask('flask_celery', template_folder=str(Path(settings.BASE_DIR, "app", "templates")))
    app.config.from_object(settings)
    init_logs(app)
    register_blueprints(app)
    init_celery(app, celery)
    register_mongo(app)
    register_jwt(app)

    return app

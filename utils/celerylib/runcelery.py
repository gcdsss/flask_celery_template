#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from utils.celerylib import celery
from app import create_app
from utils.celerylib.celery_util import init_celery
app = create_app()
init_celery(app, celery)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Blueprint
from utils.celerylib.tasks.base import test_task

base_service = Blueprint("base_service", __name__)


@base_service.route("/", methods=["GET"])
def hello():
    return "Hello, World!"


@base_service.route("/celery", methods=["GET"])
def async_hello():
    test_task.delay()
    return "Hello, World! Celery!"

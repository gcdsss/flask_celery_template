#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from app.controllers import base_service
# from .apps.PISAPPLYServices.pis_apply import pis_apply_services


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(base_service)

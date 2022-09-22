from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.signals import after_setup_logger
celery = Celery('pis_middle_layer', config_source='utils.celerylib.celery_config')

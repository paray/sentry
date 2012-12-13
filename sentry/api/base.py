#
# Created on 2012-12-3
#
# @author: hzyangtk@corp.netease.com
#

import json

from sentry.file_cache import setting_list
from sentry.openstack.common import log as logging


LOG = logging.getLogger(__name__)


def get_product_metric_list():
    """Return product metric list of sentry and monitor"""
    settings = setting_list.get_setting_list()
    metric_list = settings.get('product_metric_list', [])
    return json.dumps(metric_list)


def get_platform_metric_list():
    """Return platform metric list of sentry and monitor"""
    settings = setting_list.get_setting_list()
    metric_list = settings.get('platform_metric_list', [])
    return json.dumps(metric_list)


def get_product_alarm_event_list():
    """Return product alarm event list of sentry"""
    settings = setting_list.get_setting_list()
    alarm_event_list = settings.get('product_alarm_event_list', [])
    return json.dumps(alarm_event_list)


def get_platform_alarm_event_list():
    """Return platform alarm event list of sentry"""
    settings = setting_list.get_setting_list()
    alarm_event_list = settings.get('platform_alarm_event_list', [])
    return json.dumps(alarm_event_list)

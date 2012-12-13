#
# Created on 2012-11-16
#
# @author: hzyangtk
#

import json

from sentry.filter.filter import Filter
from sentry.openstack.common import log
from sentry.openstack.common import cfg

CONF = cfg.CONF

alarm_filter_configs = [
    cfg.StrOpt('alarm_filter_config', default='/etc/sentry/filter/alarm_filter.conf'),
]

CONF.register_opts(alarm_filter_configs)


LOG = log.getLogger(__name__)


class AlarmFilter(Filter):
    '''
    Filter for alarm system
    '''

    def __init__(self):
        '''
        init filter rules
        '''
        self.init_filter()
        self.register_filter()

    def init_filter(self):
        json_data = open(CONF.alarm_filter_config, 'r').read()
        dict_data = json.loads(json_data)
        self.filter_reject_rule = dict_data['sentry_reject_levels']
        self.filter_accept_rule = dict_data['sentry_accept_levels']

    def register_filter(self):
        self.filters = []
        self.filters.append(self._error_reject_filter)
        self.filters.append(self._warn_reject_filter)
        self.filters.append(self._info_reject_filter)

    def filter(self, flow_data):
        for filter_func in self.filters:
            if flow_data is None:
                return
            flow_data = filter_func(flow_data)
        return flow_data

    def _error_reject_filter(self, flow_data):
        if flow_data is None:
            return
        if flow_data['alarm_type'] not in self.filter_reject_rule['ERROR']:
            return flow_data
        else:
            return

    def _warn_reject_filter(self, flow_data):
        if flow_data is None:
            return
        if flow_data['alarm_type'] not in self.filter_reject_rule['WARN']:
            return flow_data
        else:
            return

    def _info_reject_filter(self, flow_data):
        if flow_data is None:
            return
        if flow_data['alarm_type'] not in self.filter_reject_rule['INFO']:
            return flow_data
        else:
            return

    def _accept_filter(self, flow_data):
        # TODO(hzyangtk): accept filter is not supported.
        return flow_data

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

owner_filter_configs = [
    cfg.StrOpt('owner_filter_config',
               default='/etc/sentry/filter/owner_filter.conf'),
]

CONF.register_opts(owner_filter_configs)


LOG = log.getLogger(__name__)


class OwnerFilter(Filter):
    """
    Filter for alarm owner
    """

    def __init__(self):
        """
        init filter rules
        """
        self.init_filter()
        self.register_filter()

    def init_filter(self):
        json_data = open(CONF.owner_filter_config, 'r').read()
        dict_data = json.loads(json_data)
        self.product_manager_rule = dict_data['product_manager']
        self.platform_manager_rule = dict_data['platform_manager']

    def register_filter(self):
        self.filters = []
        self.filters.append(self._product_manager_filter)
        self.filters.append(self._platform_manager_filter)

    def filter(self, flow_data):
        for filter_func in self.filters:
            if flow_data is None:
                return
            flow_data = filter_func(flow_data)
        return flow_data

    def _product_manager_filter(self, flow_data):
        """
        When the level not appear in the product manager level rule,
        return None.
        When the type appear in the product manager forbidden rule,
        return None.(Black list)
        Else return flow_data.
        """
        if flow_data['alarm_level'] in self.product_manager_rule:
            if flow_data['alarm_type'] not in \
                self.product_manager_rule[flow_data['alarm_level']]:
                flow_data['alarm_owner'].append('product_manager')
        return flow_data

    def _platform_manager_filter(self, flow_data):
        """
        When the level not appear in the platform manager level rule,
        return None.
        When the type appear in the platform manager forbidden rule,
        return None.(Black list)
        Else return flow_data.
        """
        if flow_data['alarm_level'] in self.platform_manager_rule:
            if flow_data['alarm_type'] not in \
                self.platform_manager_rule[flow_data['alarm_level']]:
                flow_data['alarm_owner'].append('platform_manager')
        return flow_data

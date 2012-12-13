#
# Created on 2012-11-16
#
# @author: hzyangtk
#

import eventlet
from eventlet import greenpool

from sentry.controller import handler
from sentry.openstack.common import cfg
from sentry.openstack.common import log
from sentry.openstack.common import rpc

"""
    Sentry listenning on rabbitmq and receive notification
    from nova-compute, nova-service-monitor, nova-cloudwatch,
    nova-network, nova-billing, nova-api, nova-scheduler.
    When received a notification, it will filter the notification
    and send a alarm message to alarm system when the notification
    is alarm level.
"""


manager_configs = [
    cfg.StrOpt('queue_suffix',
               default='sentry',
               help='Name of queue suffix'),
    cfg.StrOpt('notifications_topic',
               default='notifications.*',
               help='Name of notifications topic'),
]


CONF = cfg.CONF
CONF.register_opts(manager_configs)
LOG = log.getLogger(__name__)


class Manager(object):

    def __init__(self):
        self.conn = rpc.create_connection(new=True)

    def serve(self):
        """
        The default notification topic is:
            "topic = '%s.%s' % (topic, priority)"

        Example:
            "notifications.info"
        """
        LOG.info('Start sentry')
        topic = CONF.notifications_topic
        LOG.info('Queue: "%s" listen on topic: "%s"' %
                 (self.get_queue_name(topic), topic))
        self.conn.declare_topic_consumer(
                topic=topic, callback=handler.Handler().handle_message,
                queue_name=self.get_queue_name(topic))
        self.conn.consume_in_thread()

    def create(self):
        return eventlet.spawn(self.serve())

    def cleanup(self):
        LOG.info('Cleanup sentry')
        rpc.cleanup()

    def get_queue_name(self, topic):
        return '%s_%s' % (topic, CONF.queue_suffix)

#
# Created on 2012-11-16
#
# @author: hzyangtk@corp.netease.com
#

import time

from sentry.sender import handler
from sentry.sender import http_sender
from sentry.openstack.common import log
from sentry.openstack.common import cfg


CONF = cfg.CONF


sender_configs = [
    cfg.MultiStrOpt('platform_project_id',
                    default=[],
                    help='Platform manager project ids'),
]


CONF.register_opts(sender_configs)
LOG = log.getLogger(__name__)
NEED_NOT_ALARM = ['RDS', 'DDB']
PLATFORM_MANAGER = ['platform_manager']
PRODUCT_MANAGER = ['product_manager']


def send_alarm(message):
    """
    The Message Example:
    {
        'message_id': str(uuid.uuid4()),
        'event_type': 'compute.create_instance',
        'publisher_id': 'compute.host1',
        'timestamp': timeutils.utcnow(),
        'priority': 'INFO',
        'payload': {'instance_id': 12, ... }
    }
    """
    format_data = data_formater(message)
    LOG.info("format_data: %s" % str(format_data))
    alarm_owner = message.get('alarm_owner')
    if format_data['namespace'] not in NEED_NOT_ALARM and alarm_owner:
        for owner in alarm_owner:
            if owner in PRODUCT_MANAGER:
                http_sender.product_send_alarm(format_data)
            elif owner in PLATFORM_MANAGER:
                for project_id in CONF.platform_project_id:
                    format_data['projectId'] = project_id
                    http_sender.platform_send_alarm(format_data)


def data_formater(message):
    """
    Data description of format_data:
    format_data: {
            "projectId":"",
            "namespace":"",
            "alarmType":"",
            "alarmTime":"",
            "alarmContent":"",
            "alarmContentSummary":"",
            "identifier":""
    }
    """
    try:
        LOG.debug("Alarm data: %s" % message)

        if handler.is_instance_down(message):
            project_id = message['payload']['project_id']
            namespace = 'openstack'
            alarm_type = 'ERROR'
            alarm_time = long(time.time() * 1000)
            alarm_content = _('Instance is down with instance uuid: %s') % \
                                                message['payload']['uuid']
            alarm_content_summary = _('Instance is down with instance uuid: '
                                      '%s') % message['payload']['uuid']
            identifier = message['payload']['uuid']
        else:
            service_name = message.get('publisher_id', 'unknown').split('.')[0]
            if 'metadata' in message['payload']:
                metadatas = message['payload']['metadata']
                namespace = 'openstack'
                for metadata in metadatas:
                    if metadata['key'] == 'service':
                        namespace = metadata['value']
                identifier = message['payload']['instance_id']
                project_id = message['payload']['tenant_id']
            else:
                instance_properties = \
                    message['payload']['request_spec']['instance_properties']
                namespace = instance_properties['metadata'].get('service',
                                                                'openstack')
                identifier = \
                        message['payload']['request_spec']['instance_uuids'][0]
                project_id = instance_properties['project_id']
            alarm_type = message['priority']
            alarm_time = long(time.time() * 1000)
            alarm_content = ("In service <%s>, when do action %s occurs this"
                             " incident. Alarm level is %s.") \
                            % (service_name, message['event_type'],
                               message['priority'])
            alarm_content_summary = ("%s occurs an incident") \
                                        % (message['event_type'])
    except KeyError:
        raise

    format_data = {
            "projectId": project_id,
            "namespace": namespace,
            "alarmType": alarm_type,
            "alarmTime": alarm_time,
            "alarmContent": alarm_content,
            "alarmContentSummary": alarm_content_summary,
            "identifier": identifier
    }
    return format_data

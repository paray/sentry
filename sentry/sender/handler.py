#
# Created on 2012-12-11
#
# @author: hzyangtk@corp.netease.com
#


def is_instance_down(message):
    if message.get('event_type') == 'monitor.vm.down':
        return True
    else:
        return False


def is_create_error():
    pass

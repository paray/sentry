#
# Created on 2012-11-16
#
# @author: hzyangtk
#

import os

from sentry.openstack.common import log as logging


LOG = logging.getLogger(__name__)


ALARM_LEVEL = ['INFO', 'WARN', 'ERROR', 'FATAL']


def get_alarm_level(level):
    """
    To get needed alarm levels, like level='ERROR', it
    will return ['ERROR', 'FATAL']
    """
    need_alarm_level = []
    level_index = ALARM_LEVEL.index(level)
    for i in range(level_index, len(ALARM_LEVEL)):
        need_alarm_level.append(ALARM_LEVEL[i])
    return need_alarm_level


def read_cached_file(filename, cache_info, reload_func=None):
    """Read from a file if it has been modified.

    :param cache_info: dictionary to hold opaque cache.
    :param reload_func: optional function to be called with data when
                        file is reloaded due to a modification.

    :returns: data from file

    """
    mtime = os.path.getmtime(filename)
    if not cache_info or mtime != cache_info.get('mtime'):
        LOG.debug(_("Reloading cached file %s") % filename)
        with open(filename) as fap:
            cache_info['data'] = fap.read()
        cache_info['mtime'] = mtime
        if reload_func:
            reload_func(cache_info['data'])
    return cache_info['data']

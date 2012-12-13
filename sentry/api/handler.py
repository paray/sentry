# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Sentry request handler."""
import webob.dec
import webob.exc

from sentry.api import base
from sentry.api import wsgi
from sentry.openstack.common import log as logging


LOG = logging.getLogger(__name__)


class SentryRequestHandler(wsgi.Application):
    """Serve metadata."""

    def __init__(self):
        LOG.info(_("sentry api handler init"))

    @webob.dec.wsgify(RequestClass=wsgi.Request)
    def __call__(self, req):
        if req.method == 'GET' and req.path_info == '/get-metric-list':
            LOG.debug(_("request from %s") % req.remote_addr)
            return base.get_metric_list()
        elif req.method == 'GET' and req.path_info == '/get-alarm-event-list':
            LOG.debug(_("request from %s") % req.remote_addr)
            return base.get_alarm_event_list()
        else:
            msg = _("Bad request")
            raise webob.exc.HTTPBadRequest(explanation=msg)

import logging

from flask import url_for, request
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource, ListResource


logger = logging.getLogger(__name__)


class ZohoListResource(ListResource):

    def build_headers(self, model):
        return {'Location': url_for('zoho', uuid=model.id, _external=True)}

    @required_acl('confd.zoho.read')
    def get(self):
        pass







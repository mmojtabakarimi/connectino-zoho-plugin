import logging

from .zoho.resource import ZohoListResource


from .db import init_db

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info('Connectino zoho plugin start loading')
        init_db(
            'postgresql://asterisk:proformatique@localhost/asterisk?application_name=wazo-zoho-plugin')
        api = dependencies['api']


        # Ratings
        api.add_resource(
            ZohoListResource,
            '/zoho',
            endpoint='zoho',

        )


        logger.info('Connectino zoho plugin loaded successfully')

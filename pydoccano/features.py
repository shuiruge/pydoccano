from .base_api import BaseAPI


class Features(BaseAPI):

    def __init__(self, doccano):
        super().__init__(doccano.session, doccano.address, doccano.version)
        self.base_endpoint = "features"

    @property
    def details(self):
        return self._get(self.base_endpoint)

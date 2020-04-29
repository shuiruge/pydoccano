from .base_api import API


class Features(API):

    def __init__(self, doccano):
        super().__init__(doccano)
        self.doccano = doccano

    @property
    def _base_endpoint(self):
        return "features"

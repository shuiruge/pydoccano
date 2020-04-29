from pydoccano.base_api import API


class Users(API):

    def __init__(self, doccano):
        super().__init__(doccano)
        self.doccano = doccano

    @property
    def _base_endpoint(self):
        return "users"

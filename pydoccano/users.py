from pydoccano.base_api import BaseAPI


class Users(BaseAPI):

    def __init__(self, doccano):
        super().__init__(doccano.session, doccano.address, doccano.version)
        self.doccano = doccano
        self.base_endpoint = "users"

    def __getitem__(self, i):
        return User(self, i)

    def __delitem__(self, i):
        return self._delete(f"{self.base_endpoint}/{i}")

    def __len__(self):
        return len(self.details)

    @property
    def details(self):
        return self._get(self.base_endpoint)


class User(BaseAPI):

    def __init__(self, doccano, id: int):
        super().__init__(doccano.session, doccano.address, doccano.version)
        self.doccano = doccano
        self.id = id
        self.base_endpoint = f"users/{self.id}"

    @property
    def details(self):
        return self._get(self.base_endpoint)

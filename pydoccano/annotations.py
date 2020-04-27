from .base_api import BaseAPI


class Annotations(BaseAPI):

    def __init__(self, document):
        super().__init__(document.session, document.address, document.version)
        self.document = document
        self.base_endpoint = f"{self.document.base_endpoint}/annotations"

    def __getitem__(self, i):
        return Annotation(self.document, i + 1)

    def __delitem__(self, i):
        return self._delete(f"{self.base_endpoint}/{i + 1}")

    def __len__(self):
        return max([_['id'] for _ in self.details])

    @property
    def details(self):
        return self._get(self.base_endpoint)


class Annotation(BaseAPI):

    def __init__(self, document, id: int):
        super().__init__(document.session, document.address, document.version)
        self.document = document
        self.id = id
        self.base_endpoint = (
            f"{self.document.base_endpoint}/annotations/{self.id}")

    @property
    def details(self):
        return self._get(self.base_endpoint)

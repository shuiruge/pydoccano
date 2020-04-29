from .base_api import API


class Annotations(API):

    def __init__(self, document):
        super().__init__(document)
        self.document = document

    @property
    def _base_endpoint(self):
        return f"{self.document._base_endpoint}/annotations"

    def __iter__(self):
        return iter(self.details)

    def __getitem__(self, position):
        return self.details[position]

    def __len__(self):
        return len(self.details)

    def append(self, annotation: dict):
        annotation = annotation.copy()
        del annotation['id']
        del annotation['user']
        del annotation['document']
        self._post(self._base_endpoint, json=annotation)

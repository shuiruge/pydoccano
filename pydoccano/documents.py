from pydoccano.base_api import BaseAPI
from pydoccano.annotations import Annotations


class Documents(BaseAPI):

    def __init__(self, project):
        super().__init__(project.session, project.address, project.version)
        self.project = project
        self.base_endpoint = f"{self.project.base_endpoint}/docs"

    def __getitem__(self, i):
        return Document(self.project, i + 1)

    def __delitem__(self, i):
        return self._delete(f"{self.base_endpoint}/{i + 1}")

    def __len__(self):
        return self.details['count']

    @property
    def details(self):
        return self._get(self.base_endpoint)


class Document(BaseAPI):

    def __init__(self, project, id: int):
        super().__init__(project.session, project.address, project.version)
        self.project = project
        self.id = id
        self.base_endpoint = f"{self.project.base_endpoint}/docs/{id}"

    @property
    def details(self):
        return self._get(self.base_endpoint)

    @property
    def annotations(self):
        return Annotations(self)


def create_document(project, text: str, annotations: [dict] = None):
    if annotations is None:
        annotations = []
    url = f"projects/{self.project.id}/docs"
    data = {'text': text, 'annotations': annotations}
    return project._post(url, json=data)

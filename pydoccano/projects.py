from pydoccano.base_api import BaseAPI
from pydoccano.documents import Documents
from pydoccano.roles import Roles
from pydoccano.labels import Labels


class Projects(BaseAPI):

    def __init__(self, doccano):
        super().__init__(doccano.session, doccano.address, doccano.version)
        self.docanno = doccano
        self.base_endpoint = "projects"

    def __getitem__(self, i):
        return Project(self, i + 1)

    def __delitem__(self, i):
        return self._delete(endpoint=f"{self.base_endpoint}/{i + 1}")

    def __len__(self):
        return max([_['id'] for _ in self.details])

    @property
    def details(self):
        return self._get(self.base_endpoint)


class Project(BaseAPI):

    def __init__(self, doccano, id: int):
        super().__init__(doccano.session, doccano.address, doccano.version)
        self.docanno = doccano
        self.id = id
        self.base_endpoint = f"projects/{self.id}"

    @property
    def documents(self):
        return Documents(self)

    @property
    def roles(self):
        return Roles(self)

    @property
    def labels(self):
        return Labels(self)

    @property
    def details(self):
        return self._get(self.base_endpoint)


def create_project(doccano, name: str, project_type: str,
                   description='', guidline=''):
    url = f"{doccano.base_endpoint}/projects"
    mapping = {'SequenceLabeling': 'SequenceLabelingProject',
                'DocumentClassification': 'TextClassificationProject',
                'Seq2seq': 'Seq2seqProject'}
    data = {
        'name': name,
        'project_type': project_type,
        'description': description,
        'guideline': guideline,
        'resourcetype': mapping[project_type]
    }
    return api._post(url, json=data)

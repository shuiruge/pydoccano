from pydoccano.base_api import API, APICollection
from pydoccano.documents import Documents
from pydoccano.roles import Roles
from pydoccano.labels import Labels


class Projects(APICollection):

    def __init__(self, doccano):
        super().__init__(doccano)
        self.docanno = doccano

    @property
    def _base_endpoint(self):
        return "projects"

    def _get_element_by_id(self, id):
        return Project(self, id)

    def __len__(self):
        return len(self.details)


class Project(API):

    def __init__(self, doccano, id: int):
        super().__init__(doccano)
        self.docanno = doccano
        self.id = id

    @property
    def _base_endpoint(self):
        return f"projects/{self.id}"

    @property
    def documents(self):
        return Documents(self)

    @property
    def roles(self):
        return Roles(self)

    @property
    def labels(self):
        return Labels(self)


def create_project(doccano, name: str, project_type: str,
                   description='', guidline=''):
    url = f"{doccano._base_endpoint}/projects"
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

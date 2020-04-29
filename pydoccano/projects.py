from pydoccano.base_api import API, APICollection
from pydoccano.documents import Documents
from pydoccano.roles import Roles
from pydoccano.labels import Labels


class Projects(APICollection):

    def __init__(self, doccano):
        super().__init__(doccano)
        self.doccano = doccano

    @property
    def _base_endpoint(self):
        return "projects"

    def _get_element_by_id(self, id):
        return Project(self, id)

    def __len__(self):
        return len(self.details)

    def add(self, value):
        if isinstance(value, dict):
            name = value['name']
            project_type = value['project_type']
            description = value.get('description', 'No description.')
            guideline = value.get('guideline', 'No guideline.')
            return _create_project(
                self, name, project_type, description, guideline)
        else:
            return super().add(value)


class Project(API):

    def __init__(self, doccano, id: int):
        super().__init__(doccano)
        self.doccano = doccano
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


class ProjectType:
    pass


class SequenceLabeling(ProjectType):
    pass


class DocumentClassification(ProjectType):
    pass


class Seq2seq(ProjectType):
    pass


def _create_project(projects: Projects, name: str, project_type: ProjectType,
                    description: str, guideline: str):
    mapping = {
        'SequenceLabeling': 'SequenceLabelingProject',
        'DocumentClassification': 'TextClassificationProject',
        'Seq2seq': 'Seq2seqProject',
    }
    project_type = project_type.__name__
    data = {
        'name': name,
        'project_type': project_type,
        'description': description,
        'guideline': guideline,
        'resourcetype': mapping[project_type],
    }
    projects._post(projects._base_endpoint, json=data)

from pydoccano.base_api import API, APICollection
from pydoccano.annotations import Annotations


class Documents(APICollection):

    def __init__(self, project):
        super().__init__(project)
        self.project = project

    @property
    def _base_endpoint(self):
        return f"{self.project._base_endpoint}/docs"

    def _get_element_by_id(self, id):
        return Document(self.project, id)

    def __len__(self):
        return self.details['count']

    def __setitem__(self, id, value):
        """Doccano restful api will not update the annotations.
        So, this assignment only changes the "text"'s value.
        """
        super().__setitem__(id, value)

class Document(API):

    def __init__(self, project, id: int):
        super().__init__(project)
        self.project = project
        self.id = id

    @property
    def _base_endpoint(self):
        return f"{self.project._base_endpoint}/docs/{self.id}"

    @property
    def annotations(self):
        return Annotations(self)

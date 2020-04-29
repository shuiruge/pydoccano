from .base_api import API, APICollection


class Labels(APICollection):

    def __init__(self, project):
        super().__init__(project)
        self.project = project

    @property
    def _base_endpoint(self):
        return f"{self.project._base_endpoint}/labels"

    def _get_element_by_id(self, id):
        return Label(self, id)

    def __len__(self):
        return len(self.details)


class Label(API):

    def __init__(self, project, id: int):
        super().__init__(project)
        self.project = project
        self.id = id

    @property
    def _base_endpoint(self):
        return f"{self.project._base_endpoint}/labels/{self.id}"

from .base_api import API, APICollection


class Roles(APICollection):

    def __init__(self, project):
        super().__init__(project)
        self.project = project

    @property
    def _base_endpoint(self):
        return f"{self.project._base_endpoint}/roles"

    def _get_element_by_id(self, id):
        return Role(self, id)

    def __len__(self):
        return len(self.details)


class Role(API):

    def __init__(self, project, id: int):
        super().__init__(project)
        self.project = project
        id = id

    @property
    def _base_endpoint(self):
        return f"{self.project._base_endpoint}/roles/{self.id}"

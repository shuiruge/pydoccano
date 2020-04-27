from .base_api import BaseAPI


class Labels(BaseAPI):

    def __init__(self, project):
        super().__init__(project.session, project.address, project.version)
        self.project = project

        self.base_endpoint = f"{self.project.base_endpoint}/labels"

    def __getitem__(self, i):
        return Label(self, i + 1)

    def __delitem__(self, i):
        return self._delete(f"{self.base_endpoint}/{i + 1}")

    def __len__(self):
        return max([_['id'] for _ in self.details])

    @property
    def details(self):
        return self._get(self.base_endpoint)


class Label(BaseAPI):

    def __init__(self, project, id: int):
        super().__init__(project.session, project.address, project.version)
        self.project = project
        self.id = id

        self.base_endpoint = f"{self.project.base_endpoint}/labels/{id}"

    @property
    def details(self):
        return self._get(self.base_endpoint)

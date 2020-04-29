import json
from typing import Union, Iterator
from requests import Session, HTTPError


class APINotFoundError(Exception):
    pass


ID = int


class BaseAPI:

    def __init__(self, session: Session, address: str, version: str):
        self._session = session
        self._address = address
        self._version = version

        self._base_url = f"{self._address.strip('/')}/{self._version}"

    def _get(self, endpoint: str, params: dict = None) -> dict:
        url = f"{self._base_url}/{endpoint}"
        response = self._session.get(url=url, params=params)
        if response.status_code == 404:  # not found.
            raise APINotFoundError()
        response.raise_for_status()
        return response.json()

    def _post(self, endpoint: str, data: dict = None, files: dict = None,
              json: dict = None) -> dict:
        url = f"{self._base_url}/{endpoint}"
        response = self._session.post(
            url=url, data=data, files=files, json=json)
        response.raise_for_status()
        return response.json()

    def _delete(self, endpoint: str):
        url = f"{self._base_url}/{endpoint}"
        response = self._session.delete(url=url)
        response.raise_for_status()

    def _put(self, endpoint: str, data : dict = None, json: dict = None) -> dict:
        url = f"{self._base_url}/{endpoint}"
        response = self._session.put(url=url, data=data, json=json)
        response.raise_for_status()
        return response.json()


class API(BaseAPI):

    def __init__(self, base_api: BaseAPI):
        super().__init__(base_api._session, base_api._address, base_api._version)
        self._base_api = base_api

    @property
    def _base_endpoint(self) -> str:
        return NotImplemented

    @property
    def details(self) -> dict:
        return self._get(self._base_endpoint)

    def __repr__(self):
        if self.details is None:
            return super().__repr__()
        return json.dumps(self.details, ensure_ascii=False)


class APICollection(API):

    def __init__(self, base_api: BaseAPI):
        super().__init__(base_api)

    def _get_element_by_id(self, id: ID) -> API:
        return NotImplemented

    def __len__(self):
        return NotImplemented

    def __getitem__(self, id: ID) -> API:
        item = self._get_element_by_id(id)
        if item.details is None:
            raise KeyError
        return item

    def __setitem__(self, id, value: Union[dict, API]):
        if isinstance(value, API):
            value = value.details.copy()
        del value['id']
        if id not in self:
            raise KeyError
        self._put(f"{self._base_endpoint}/{id}", json=value)

    def __delitem__(self, id: ID):
        self._delete(f"{self._base_endpoint}/{id}")

    def __iter__(self) -> Iterator[ID]:
        return self._get_id_generator()

    def _get_id_generator(self):
        id = 1
        n = 0
        while n < len(self):
            try:
                n += 1
                yield id
            except KeyError:
                pass
            id += 1

    def add(self, value: Union[dict, API]):
        if isinstance(value, API):
            value = value.details.copy()
        del value['id']
        self._post(self._base_endpoint, json=value)

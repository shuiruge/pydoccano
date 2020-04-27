import json
from requests import Session, HTTPError


class BaseAPI:

    def __init__(self, session: Session, address: str, version: str):
        self.session = session
        self.address = address
        self.version = version

        self.base_url = f"{address.strip('/')}/{version}"

    def _get(self, endpoint: str, params: dict = None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url=url, params=params)
        if response.status_code == 404:  # not found.
            return None
        response.raise_for_status()
        return response.json()

    def _post(self, endpoint: str, data: dict = None, files: dict = None,
              json: dict = None) -> json:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url=url, data=data, files=files, json=json)
        response.raise_for_status()
        return response.json()

    def _delete(self, endpoint: str) -> json:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.delete(url=url)
        response.raise_for_status()
        return response.json()

    def _put(self, endpoint: str, data : dict = None) -> json:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.put(url=url, data=data)
        response.raise_for_status()
        return response.json()

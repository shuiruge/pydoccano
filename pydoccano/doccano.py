from requests import Session
from requests.models import Response

from pydoccano.base_api import BaseAPI
from pydoccano.users import Users
from pydoccano.projects import Projects
from pydoccano.features import Features


class Doccano(BaseAPI):
    def __init__(self, address: str, username: str, password: str, version='v1'):
        super().__init__(Session(), address, version)
        self._login(username, password)

    @property
    def users(self):
        return Users(self)

    @property
    def projects(self):
        return Projects(self)

    @property
    def features(self):
        return Features(self)

    @property
    def me(self):
        return self._get(endpoint="me")

    def _login(self, username: str, password: str) -> Response:
        auth = {
            'username': username,
            'password': password
        }
        response_json = self._post(endpoint='auth-token', data=auth)
        token = response_json['token']
        self.session.headers.update(
            {
                'Authorization': f"Token {token}",
                'Accept': 'application/json'
            }
        )

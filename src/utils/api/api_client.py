from abc import ABC
from collections.abc import Iterable, Mapping
from http import HTTPMethod
from typing import TypeAlias

import backoff
import requests

from yarl import URL

PrimitiveData: TypeAlias = str | int | float | bool | None
JsonType: TypeAlias = Mapping[str, "JsonType"] | Iterable["JsonType"] | PrimitiveData


class HTTPClient(ABC):
    base_url: str

    def __init__(self, base_url: str):
        self.base_url = base_url

    @backoff.on_exception(
        backoff.constant,
        exception=requests.HTTPError,
        interval=3,
        max_tries=5,
    )
    def make_request(
        self,
        method: HTTPMethod,
        path: str,
        query: dict | None = None,
        headers: Mapping[str, str | bytes | None] | None = None,
        payload: JsonType = None,
        json: JsonType = None,
        files: list | None = None,
        *,
        check_response_status: bool = False,
        verify: bool = False,
    ) -> requests.models.Response:
        """Выполнение http-запроса."""
        response = requests.request(
            method,
            url=str(URL(self.base_url).with_path(path).with_query(query)),
            headers=headers,
            data=payload,  # type: ignore[arg-type]
            json=json,
            files=files,
            verify=verify,
        )
        if check_response_status:
            response.raise_for_status()
        return response

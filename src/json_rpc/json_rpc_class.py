from typing import Optional

import requests
from requests import Timeout, Response


class JsonRPC:
    """
    Класс для работы с API Data, через Json-RPC
    """

    def __init__(
            self,
            *,
            url: str | None = '',
            api_prefix: str | None = '',
            request_id: int | None = 0,
            json_rpc_version: str | None = "2.0",
    ) -> None:
        """

        :param url: url до api "https://my-api.com"
        :param api_prefix: "https://my-api.com/v1/api/form" example: "/v1/api/form"
                                              |___________|
        """
        self.__base_url = url if url else 'https://my-extralogic-data-1.herokuapp.com'
        self.__api_prefix = api_prefix if api_prefix else '/api/form'
        self.__api_url = self.__api_url(url=self.__base_url, api_prefix=self.__api_prefix)
        self._request_id = request_id
        self._json_rpc_version = json_rpc_version
        self._timeout = 30

    def get_fields(self, form_uid: str):
        """
        Получение формы и ее полей
        :param form_uid:
        :return:
        """
        method = 'form.get_fields'
        params = {'form_uid': form_uid}

        response = self.__call_api(method=method, params=params)

        return response

    def get_form_data(self, form_uid: str):
        """
        Получение формы, ее полей и значений полей
        :param form_uid:
        :return:
        """
        method = 'form.get_form_data'
        params = {'form_uid': form_uid}

        response = self.__call_api(method=method, params=params)

        return response

    def update_value_fields(self, value_fields: list):
        """
        Отправка значений у полей

        :param value_fields:
        [
        {
            id: 1,
            value_field: "value_1"
        },
        {
            id: 2,
            value_field: "value_2"
        }
        ]
        :return:
        """
        method = 'form.update_value_fields_by_id'
        params = {'value_fields': value_fields}

        response = self.__call_api(method=method, params=params)

        return response

    def set_request_id(self, request_id: int) -> None:
        """
        Setter for Json-RPC "id"
        :param request_id: id
        :return:
        """
        self._request_id = request_id

    @staticmethod
    def __api_url(url, api_prefix) -> str:
        """
        Собирает полный url до места вызова json-rpc
        """
        return f'{url}{api_prefix}'

    def __call_api(self, method: str, params: dict) -> Optional[Response]:
        response = None

        body = {
            'method': method,
            'jsonrpc': self._json_rpc_version,
            'id': self._request_id,
            'params': params
        }

        try:
            response = requests.post(self.__api_url, json=body, timeout=self._timeout)
        except Timeout as e:
            print(e)

        return response

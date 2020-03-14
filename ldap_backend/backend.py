# -*- coding: utf-8 -*-
import requests

from ldap_backend.conf import settings


class LdapBackend:
    """
        Options:
                username - Username from your LDAP
                password - Password from your LDAP
        Response:
            response status from the server and data
            if response 200
                get all data from ldap
            else
                return str error

    """

    @staticmethod
    def authorization(username, password, token):

        if not token:
            if not settings.TOKEN_LDAP:
                raise Exception("* Please enter the Token")

            token = settings.TOKEN_LDAP

        try:
            response = requests.post(
                f"{settings.HOST_LDAP}/auth",
                json={'username': username,
                      'password': password,
                      'token': token})

        except requests.exceptions.ConnectionError as err:
            return 404, err

        if response.status_code == 200:
            return response.status_code, response.json()

        else:
            return response.status_code, response.content

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

from ldap_backend.backend import LdapBackend
from ldap_backend.conf import settings


def authorization_ldap(username, password, token=""):
    with LdapBackend() as ldap_requests:
        return ldap_requests.authorization(username, password, token)


def set_setting(setting_name, setting_value):
    with settings as settings_setup:
        return settings_setup.set(setting_name, setting_value)


def set_setting_from_dict(dict_):
    with settings as settings_setup:
        return settings_setup.from_dict(dict_)


def set_setting_from_object(obj):
    with settings as settings_setup:
        return settings_setup.from_object(obj)

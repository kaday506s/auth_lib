from ldap_backend.conf import (
    LazySettings,
    settings as ldap_settings,
)


class DjangoLazySettings(LazySettings):
    def _setup(self):
        from django.conf import settings as django_settings

        ldap_settings.from_object(django_settings)
        self._wrapped = ldap_settings


settings = DjangoLazySettings()

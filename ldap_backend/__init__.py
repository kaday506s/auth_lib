from .api import authorization_ldap

__version__ = '0.3.4'

__description__ = """
The library is intended for authorization in LDAB through the backend

In your DJANGO application in the file settings.py append
AUTHENTICATION_BACKENDS = (
                        * * *
        'ldap_backend.django.backends.AuthenticationBackend'
        )

In your django application in setting.py append add 2 lines to work with 
the library:

    Example:
        TOKEN_LDAP="TOKEN*"  - Token to connection with backend
        HOST_LDAP="URL*" - Url backend 

"""

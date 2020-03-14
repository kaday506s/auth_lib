In your DJANGO application in the file settings.py append:

    Example:
            AUTHENTICATION_BACKENDS = (
                    * * *
                'ldap_backend.django.backend.AuthenticationBackend',
            )
            
       AND
            INSTALLED_APPS = [
                    * * *
                'ldap_backend'
            ]
            
AND append in setting.py 2 lines to work with
the library:

    Example:
        TOKEN_LDAP = 'TOKEN*'  - Token to connection with backend
        HOST_LDAP = 'URL*'     - Url backend
        
**(Optional)** If You want update information about USER you can write your map fields USER_MAP_LDAP in settings.py:
- First value is field from LDAP.
- Second Value is field your Model User.

    
    Example:
        'USER_MAP_LDAP': {
            'mail': 'email',
            'sAMAccountName': 'username',
            'givenName': 'first_name'
        }
 
**(Optional)** In other projects, you can use api:

        Example:
        
            from ldap_backend.api import (set_setting, 
                                          authorization_ldap, 
                                          set_setting_from_dict,
                                          set_setting_from_object
                                          )
                                          
            # First option
            set_setting('HOST_LDAP', 'http://127.0.0.1:8010')
            set_setting_from_dict({'TOKEN_LDAP': 'c1279bb9b844a6a94b1024a52348236a'})
            
            # Second option
            class ValueSetting:
                HOST_LDAP = 'http://127.0.0.1:8010'
                TOKEN_LDAP = 'c1279bb9b844a6a94b1024a52348236a'
                
            set_setting_from_object(ValueSetting)
            
            status, res = authorization_ldap('username', 'password')
        
        or 
            # First option
            from ldap_backend import authorization_ldap
            from ldap_backend.conf import settings
            
            settings.set('HOST_LDAP', 'http://127.0.0.1:8010')
            settings.from_dict({'TOKEN_LDAP': 'c1279bb9b844a6a94b1024a52348236a'})
            
            # Second option
            class ValueSetting:
                HOST_LDAP = 'http://127.0.0.1:8010'
                TOKEN_LDAP = 'c1279bb9b844a6a94b1024a52348236a'
                
            set_setting_from_object(ValueSetting)
            status, res =  authorization_ldap('username', 'password')

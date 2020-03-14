try:
    from django.contrib.auth.backends import ModelBackend
except:
    class ModelBackend:
        pass


from ldap_backend.backend import LdapBackend
from ldap_backend.django.conf import settings


class AuthenticationBackend(ModelBackend):
    """
    Function to include with your Django app

    Example in file setting.py append

        AUTHENTICATION_BACKENDS = (
                        * * *
            'ldap_backend.django.backend.AuthenticationBackend'
        )
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        from django.contrib.auth import get_user_model
        User = get_user_model()

        status, data = LdapBackend.authorization(
            username, password, settings.TOKEN_LDAP
        )

        if status == 200:
            try:
                user = User.objects.get(username__iexact=username)
            except User.DoesNotExist:
                return None
            else:
                for ldap_field, user_field in settings.USER_MAP_LDAP.items():
                    if hasattr(user, user_field):
                        if data.get(ldap_field):
                            setattr(user, user_field, data.get(ldap_field))
                user.is_staff = True
                user.save()
                return user
        else:
            return None

    def get_user(self, user_id):
        from django.contrib.auth import get_user_model
        User = get_user_model()

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

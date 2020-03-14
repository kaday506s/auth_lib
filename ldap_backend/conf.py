from ldap_backend import global_settings


class LazySettings:
    def __init__(self):
        self._wrapped = None

    def _setup(self):
        self._wrapped = Settings()

    def __getattr__(self, item):
        if self._wrapped is None:
            self._setup()
        return getattr(self._wrapped, item)

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass


class Settings:
    def __init__(self):
        self._settings_names = []

        for setting_name in dir(global_settings):
            if setting_name.isupper():
                setting_value = getattr(global_settings, setting_name)
                setattr(self, setting_name, setting_value)
                self._settings_names.append(setting_name)

    def from_object(self, obj):
        for setting_name in self._settings_names:
            if hasattr(obj, setting_name):
                setting_value = getattr(obj, setting_name)
                self.set(setting_name, setting_value)

    def from_dict(self, dict_):
        for setting_name in self._settings_names:
            if setting_name in dict_:
                setting_value = dict_[setting_name]
                self.set(setting_name, setting_value)

    def set(self, setting_name, setting_value):
        setting_value = self._validate(
            setting_name, setting_value,
        )
        setattr(self, setting_name, setting_value)

    def _validate(self, setting_name, setting_value):
        if setting_name == "HOST_LDAP":
            if setting_value[-1] == '/':
                setting_value = setting_value[:-1]

        elif setting_name == "TOKEN_LDAP":
            if setting_value is None:
                raise Exception("* Please enter the Token in settings.py")

        return setting_value


settings = LazySettings()

from abc import ABC, abstractmethod


class AppThemeManager(ABC):
    is_active: bool

    @property
    def friendly_name(self):
        return self.__appname__\
                if hasattr(self, '__appname__')\
                else self.__name__

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.is_active = True

    def startup(self, manager):
        if self.is_active:
            name = self.friendly_name
            print('Calling Startup: {}'.format(name))
            try:
                self.on_startup(manager)
            except Exception as e:
                print('{} Calling Startup Error: {}'.format(e, name))

    def apply_theme(self, manager):
        if self.is_active:
            name = self.friendly_name
            print('Applying theme: {}'.format(name))
            try:
                self.on_apply_theme(manager)
            except Exception as e:
                print('{} Apply Theme Error: {}'.format(e, name))

    @abstractmethod
    def on_startup(self, manager):
        pass

    @abstractmethod
    def on_apply_theme(self, manager):
        pass

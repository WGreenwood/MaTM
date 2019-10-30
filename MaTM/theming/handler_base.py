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
            print('On Startup: {}'.format(self.friendly_name))
            self.on_startup(manager)

    def apply_theme(self, manager):
        if self.is_active:
            print('Applying theme: {}'.format(self.friendly_name))
            self.on_apply_theme(manager)

    @abstractmethod
    def on_startup(self, manager):
        pass

    @abstractmethod
    def on_apply_theme(self, manager):
        pass

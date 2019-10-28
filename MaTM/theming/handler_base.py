from abc import ABC, abstractmethod


class AppThemeManager(ABC):
    is_active: bool

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.is_active = True

    def startup(self, manager):
        if self.is_active:
            self.on_startup(manager)

    def apply_theme(self, manager):
        if self.is_active:
            self.on_apply_theme(manager)

    @abstractmethod
    def on_startup(self, manager):
        pass

    @abstractmethod
    def on_apply_theme(self, manager):
        pass

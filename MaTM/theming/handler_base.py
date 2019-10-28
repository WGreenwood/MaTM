from abc import ABC, abstractmethod


class AppThemeManager(ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()

    @abstractmethod
    def on_startup(self, manager):
        pass

    @abstractmethod
    def on_apply_theme(self, manager):
        pass

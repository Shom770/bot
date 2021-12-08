from os.path import dirname

from bot.exts.filtering._settings_types.settings_entry import SettingsEntry
from bot.exts.filtering._utils import subclasses_in_package

settings_types = subclasses_in_package(dirname(__file__), f"{__name__}.", SettingsEntry)
settings_types = {settings_type.name: settings_type for settings_type in settings_types}

__all__ = [settings_types]

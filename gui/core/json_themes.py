import json
import os
import sys

# IMPORT SETTINGS
from gui.core.json_settings import Settings

class Themes(object):
    # 1. SETUP ROOT PATH
    # ///////////////////////////////////////////////////////////////
    if getattr(sys, 'frozen', False):
        # Running as Nuitka EXE - get the directory of the executable
        # Then go to the internal root
        _root_path = os.path.dirname(sys.executable)
        # Nuitka Onefile puts everything in a flat-ish structure or specific subfolders
        # We check if we are in the temp folder
        if "Temp" in _root_path or "ONEFIL" in _root_path:
             # Use the location of this specific script file to find the gui folder
             _root_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    else:
        # Running as standard Python script
        _root_path = os.path.abspath(".")

    # 2. LOAD SETTINGS
    # ///////////////////////////////////////////////////////////////
    setup_settings = Settings()
    _settings = setup_settings.items

    # 3. DEFINE PATHS AS STRINGS
    # ///////////////////////////////////////////////////////////////
    # We ensure these are forced to strings to avoid the TypeError
    themes_path = str(os.path.join(_root_path, "gui", "themes"))
    json_file_name = str(_settings['theme_name']) + ".json"
    settings_path = str(os.path.join(themes_path, json_file_name))

    # DEBUG PRINT (Optional: shows in console if --windows-console-mode=force)
    # print(f"Root: {_root_path}")
    # print(f"Themes Path: {themes_path}")

    def __init__(self):
        super(Themes, self).__init__()
        self.items = {}
        self.deserialize()

    def serialize(self):
        with open(self.settings_path, "w", encoding='utf-8') as write:
            json.dump(self.items, write, indent=4)

    def deserialize(self):
        if os.path.exists(self.settings_path):
            with open(self.settings_path, "r", encoding='utf-8') as reader:
                settings = json.loads(reader.read())
                self.items = settings
        else:
            # Fallback if the specific theme is missing
            default_path = os.path.join(self.themes_path, "default.json")
            if os.path.exists(default_path):
                with open(default_path, "r", encoding='utf-8') as reader:
                    self.items = json.loads(reader.read())

    def get_theme(self, theme_name):
        file_path = os.path.join(self.themes_path, f"{theme_name}.json")
        if not os.path.exists(file_path):
            file_path = os.path.join(self.themes_path, "default.json")

        with open(file_path, "r", encoding='utf-8') as f:
            return json.load(f)
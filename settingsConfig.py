from pathlib import Path

from decouple import config


class _SettingsConfig:
    def __init__(self):
        self.__settingsConfigDB = self.__loadSettingsDB()

    def __loadSettingsDB(self):
        __settings = {}
        __settings["LOG"] = dict(
            file=config("LOG_FILE"),
            directory=config("LOG_DIRECTORY")
        )
        __settings["DRIVERS"] = dict(
            directory=config("DRIVERS_DIRECTORY"),
            chrome=Path(config("DRIVERS_DIRECTORY")) / config("CHROME_DRIVER"),
            firefox=Path(config("DRIVERS_DIRECTORY")) / config("FIREFOX_DRIVER")
        )
        __settings["DATA"] = dict(
            directory=config("DATA_DIRECTORY"),
            pricesFile=Path(config("DATA_DIRECTORY")) / config("DATA_PRICES_FILE")
        )
        __settings["REPORTS"] = dict(
            directory=Path(config("REPORT_DIRECTORY"))
        )
        __settings["DIRECTORIES"] = [
            __settings["DATA"]["directory"],
            __settings["REPORTS"]["directory"]
        ]
        return __settings

    @property
    def LogSettings(self):
        return self.__settingsConfigDB["LOG"]

    @property
    def DriversSettings(self):
        return self.__settingsConfigDB["DRIVERS"]

    @property
    def Data(self):
        return self.__settingsConfigDB["DATA"]

    @property
    def Reports(self):
        return self.__settingsConfigDB["REPORTS"]

    @property
    def Directories(self):
        return self.__settingsConfigDB["DIRECTORIES"]


g_settingsConfig = _SettingsConfig()

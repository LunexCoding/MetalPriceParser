from collections import namedtuple

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.firefox.service import Service as firefoxService

from settingsConfig import g_settingsConfig


DRIVER = namedtuple("DRIVER", ["type", "service", "options", "driver"])


class DRIVER_TYPES:
    CHROME = 0
    FIREFOX = 1


# OPTIONS = ["--headless"]
OPTIONS = []
CHROME_OPTIONS = webdriver.ChromeOptions()
FIREFOX_OPTIONS = webdriver.FirefoxOptions()
for option in OPTIONS:
    CHROME_OPTIONS.add_argument(option)
    FIREFOX_OPTIONS.add_argument(option)


class DRIVER_SETTINGS:
    CHROME = DRIVER(
        DRIVER_TYPES.CHROME,
        chromeService(executable_path=g_settingsConfig.DriversSettings["chrome"]),
        CHROME_OPTIONS,
        webdriver.Chrome
    )
    FIREFOX = DRIVER(
        DRIVER_TYPES.FIREFOX,
        firefoxService(executable_path=g_settingsConfig.DriversSettings["firefox"]),
        FIREFOX_OPTIONS,
        webdriver.Firefox
    )

    @classmethod
    def getDriverByType(cls, driver_type):
        for driverSetting in cls.__dict__.values():
            if isinstance(driverSetting, DRIVER) and driverSetting.type == driver_type:
                return driverSetting
        return None


SELECTOR_TYPE = namedtuple("SELECTOR_TYPE", ["id", "name"])


class SELECTOR_TYPES:
    XPATH = SELECTOR_TYPE(0, "xpaths")
    CSS = SELECTOR_TYPE(1, "css")
    TAG = SELECTOR_TYPE(2, "tag")


SELECTOR = namedtuple("SELECTOR", ["name", "type", "selector"])


class SELECTORS:
    TABLE = SELECTOR("TABLE", SELECTOR_TYPES.XPATH, "/html[1]/body[1]/main[1]/section[4]/div[1]/table[1]")
    ROWS = SELECTOR("ROWS", SELECTOR_TYPES.TAG, "tr")
    ROW_DATA = SELECTOR("ROW_DATA", SELECTOR_TYPES.TAG, "td")


class Constants:
    ITEM_NAME = "Наименование"
    ITEM_PRICE = "Цена за 1КГ"

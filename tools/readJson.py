import json

from settingsConfig import g_settingsConfig


def getDataPrices():
    try:
        with open(g_settingsConfig.Data["pricesFile"], "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return None

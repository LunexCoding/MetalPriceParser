import json
from datetime import datetime

from .consts import Constants
from tools.fileSystem import FileSystem
from settingsConfig import g_settingsConfig


class Report:
    def __init__(self, metalInfoWidgets):
        self.data = {}

        self._save(metalInfoWidgets)

    def _initFields(self):
        self.data["Дата создания"] = None
        self.data["Данные"] = []

    def _addDate(self):
        date = datetime.now().strftime(Constants.DATETIME_FORMAT)
        self.data["Дата создания"] = date

    def _parseInfoFromWidget(self, widgets):
        for widget in widgets:
            metal = widget.metal
            metalRate = widget.metalRate
            count = widget.count
            price = widget.price
            self.data["Данные"].append(
                {
                    "Метал": metal,
                    "Курс": metalRate,
                    "Количество": count,
                    "Цена": price
                }
            )

    def _write(self):
        path = FileSystem.createUniqueFile(g_settingsConfig.Reports["directory"] / "Report.json")
        print(path)
        with open(path, "w", encoding="utf-8") as outfile:
            json.dump(self.data, outfile, ensure_ascii=False, indent=4)

    def _save(self, widgets):
        self._initFields()
        self._addDate()
        self._parseInfoFromWidget(widgets)
        self._write()


from customtkinter import CTkButton, CTkFrame, CTkScrollableFrame, Y, TOP, BOTH

from .context import Context
from .pricesContext import PricesContext
from storage import g_storage
from parser.consts import Constants
from ui.widgets.metalInfo import CustomMetalInfo
from tools.report import Report


class MainContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        self._metalWidgets = []

        self.frame = CTkFrame(window)
        self.scrollableFrame = CTkScrollableFrame(self.frame)
        self.buttonFrame = CTkFrame(window)

        self.openPricesContextButton = CTkButton(self.buttonFrame, text="Цены", command=self._openPricesContextButtonClicked)
        self.openPricesContextButton.pack(padx=10, pady=10)

        self.addMetalInfoWidgetButton = CTkButton(self.buttonFrame, text="Добавить металл", command=self._addMetalInfoWidgetButtonClicked)
        self.addMetalInfoWidgetButton.pack(padx=10, pady=10)

        self.buttonSave = CTkButton(self.buttonFrame, text="Сохранить", command=self._buttonSaveClicked)
        self.buttonSave.pack(padx=10, pady=10)

        self.buttonFrame.pack(padx=10, pady=10)
        self.scrollableFrame.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.frame.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)

    def _openPricesContextButtonClicked(self):
        window = self._window
        self.clear()
        window.changeContext(
            PricesContext,
            data={
                "columns": [Constants.ITEM_NAME, Constants.ITEM_PRICE],
                "data": g_storage.readData()
            }
        )

    def _addMetalInfoWidgetButtonClicked(self):
        self._metalWidgets.append(
            CustomMetalInfo(self.scrollableFrame)
        )

    def _buttonSaveClicked(self):
        Report(self._metalWidgets)

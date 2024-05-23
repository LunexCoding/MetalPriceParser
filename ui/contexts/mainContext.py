from customtkinter import CTkButton, CTkFrame, Y

from .context import Context
from .pricesContext import PricesContext
from tools.readJson import getDataPrices


class MainContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        self.frame = CTkFrame(window)

        self.openPricesContextButton = CTkButton(self.frame, text="Цены", command=self._openPricesContextButtonClicked)
        self.openPricesContextButton.pack(padx=10, pady=10)

        self.frame.pack(fill=Y, padx=10, pady=10)

    def _openPricesContextButtonClicked(self):
        window = self._window
        self.clear()
        window.changeContext(
            PricesContext,
            data={
                "columns": ["Наименование", "Цена"],
                "data": getDataPrices()
            }
        )
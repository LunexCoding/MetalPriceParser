from customtkinter import CTkBaseClass, CTkFrame, CTkComboBox, CTkEntry, CTkLabel, CTkButton

from storage import g_storage
from parser.consts import Constants


class CustomMetalInfo(CTkBaseClass):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._metal = None
        self._metalRate = 0
        self._price = 0

        self.frame = CTkFrame(master)
        self.errorLabel = CTkLabel(self.frame, text="Ошибка", text_color="red")
        values = [item["Наименование"] for item in g_storage.data]

        self.metalBox = CTkComboBox(self.frame, values=values, command=self._comboboxCallback)
        self.metalRateLabel = CTkLabel(self.frame, text=str(0.0))
        self.countEntry = CTkEntry(self.frame, placeholder_text="Кол-во")
        self.priceLabel = CTkLabel(self.frame, text=str(0))
        self.buttonCalc = CTkButton(self.frame, text="Рассчитать", command=self.calcPrice)
        self.metalBox.pack(side="left", padx=5, pady=5, fill="x", expand=True)
        self.metalRateLabel.pack(side="left", padx=5, pady=5)
        self.countEntry.pack(side="left", padx=5, pady=5)
        self.priceLabel.pack(side="left", padx=5, pady=5)
        self.buttonCalc.pack(side="left", padx=5, pady=5)
        self.frame.pack(padx=10, pady=10, fill="x", expand=True)

    def _comboboxCallback(self, choice):
        self._metal = choice
        self._metalRate = self._findMetalPrice()
        self.metalRateLabel.configure(text=str(self._metalRate))

    def calcPrice(self):
        if self.validate():
            self.errorLabel.pack_forget()
            if self._metalRate is None:
                self.priceLabel.configure(text="Ошибка")
            else:
                self._price = self._metalRate * float(self.countEntry.get())
                self.priceLabel.configure(text=str(self._price))
        else:
            self.errorLabel.pack(side="center", padx=5, pady=5)

    def _findMetalPrice(self):
        for item in g_storage.data:
            if item[Constants.ITEM_NAME] == self._metal:
                return item[Constants.ITEM_PRICE]
        return None

    def validate(self):
        if self._metal is None:
            return False
        if len(self.countEntry.get()) == 0:
            return False
        return True

    @property
    def metal(self):
        return self._metal

    @property
    def metalRate(self):
        return self._metalRate

    @property
    def count(self):
        return float(self.countEntry.get())

    @property
    def price(self):
        return self._price

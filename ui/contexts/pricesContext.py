from tkinter.ttk import Scrollbar, Treeview
from customtkinter import CTkButton, CTkFrame, Y, CENTER, VERTICAL, TOP, BOTH, RIGHT, LEFT, END

from .context import Context


class PricesContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        window.geometry("800x800")

        columns = data["columns"]
        data = data["data"]

        self.buttonBack = CTkButton(window, text="Назад", command=self._onButtonBackClicked)
        self.buttonBack.pack()

        self.tableFrame = CTkFrame(window)
        self.tree = Treeview(self.tableFrame, columns=columns)
        for header in columns:
            self.tree.heading(header, text=header)
            self.tree.column(header, anchor=CENTER)
        self.tree.column("#0", width=0, stretch=False)
        self.treeScroll = Scrollbar(self.tree, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.treeScroll.set)
        self.tree.pack(side=TOP, fill=BOTH, expand=True, pady=10, padx=10)
        self.treeScroll.pack(side=RIGHT, fill=Y)
        self.tableFrame.pack(side=LEFT, fill=BOTH, expand=True)

        if data is not None:
            for row in data:
                self.tree.insert("", END, values=list(row.values()))

    def _onButtonBackClicked(self):
        window = self._window
        self.clear()
        window.returnToPrevious()

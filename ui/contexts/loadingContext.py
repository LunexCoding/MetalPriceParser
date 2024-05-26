from customtkinter import CTkLabel

from .context import Context
from .mainContext import MainContext
from ui.widgets.progressBar import CustomProgressBar


class LoadingContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self._window = window
        CTkLabel(window, text="Loading...").pack(pady=20, padx=20)
        self.progressBar = CustomProgressBar(window, 0, 0.8, 1, 1)
        self.progressBar.pack(pady=20, padx=20)

        self.progressBar.animateProgress()

    def complete(self):
        self.progressBar.setToComplete()
        window = self._window
        self.clear()
        window.changeContext(MainContext)

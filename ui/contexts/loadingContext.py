from customtkinter import CTkLabel, DoubleVar, CTkProgressBar

from .context import Context


class LoadingContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self._window = window
        CTkLabel(window, text="Loading...").pack(pady=20, padx=20)
        self.progressVar = DoubleVar()
        self.progressBar = CTkProgressBar(self._window, variable=self.progressVar)
        self.progressBar.pack(pady=20, padx=20)
        self.progressVar.set(0)

    def updateProgress(self, value):
        self.progressVar.set(value)

    def complete(self):
        self.updateProgress(100)

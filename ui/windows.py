from customtkinter import CTk

from .contexts.mainContext import MainContext


class BaseWindow(CTk):
    def __init__(self):
        super().__init__()
        self.context = None
        self.previousContext = None

    def close(self):
        CTk.destroy(self)

    def changeContext(self, contextClass, data=None):
        if contextClass is not None:
            if self.context is not None:
                self.context.clear()
            self.previousContext = self.context.__class__
            self.context = contextClass(self, data)

    def returnToPrevious(self, data=None):
        self.changeContext(self.previousContext, data)


class MainWindow(BaseWindow):
    def __init__(self, data=None):
        super().__init__()

        self.context = MainContext(self, data)

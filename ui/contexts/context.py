class Context:
    def __init__(self, window, data):
        self._window = window
        self._data = data

    def clear(self):
        if self._window is not None:
            for widget in self._window.winfo_children():
                widget.destroy()
            self._window = None

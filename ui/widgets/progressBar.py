from customtkinter import CTkProgressBar, CTkBaseClass


class CustomProgressBar(CTkBaseClass):
    def __init__(self, master, initialValue=0, targetValue=1, finalValue=1, timesleep=1, **kwargs):
        super().__init__(master, **kwargs)

        self.progressBar = CTkProgressBar(master)
        self.progressBar.pack(pady=20)

        self.initialValue = initialValue
        self.targetValue = targetValue
        self.finalValue = finalValue
        self.timesleep = timesleep
        self.currentValue = initialValue
        self.step = (finalValue - initialValue) / (1000 / timesleep)

    def setProgress(self, value):
        if 0 <= value <= 1:
            self.progressBar.set(value)
            self.currentValue = value
        else:
            raise ValueError("Progress value must be between 0 and 1")

    def animateProgress(self):
        if (self.step > 0 and self.currentValue < self.targetValue) or (
                self.step < 0 and self.currentValue > self.targetValue):
            self.currentValue += self.step
            self.setProgress(self.currentValue)
            self.progressBar.after(self.timesleep * 10, self.animateProgress)
        else:
            self.setProgress(self.targetValue)

    def setToComplete(self):
        self.setProgress(1)

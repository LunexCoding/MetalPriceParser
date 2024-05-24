import threading
import time

from parser.parser import Parser
from settingsConfig import g_settingsConfig
from tools.fileSystem import FileSystem
from tools.fileSystemExceptions import PathExistsException
from tools.logger import logger
from ui.windows import MainWindow
from ui.contexts.mainContext import MainContext
from ui.contexts.loadingContext import LoadingContext


_log = logger.getLogger(__name__)


class App:
    def __init__(self):
        self._window = None
        self._parserThread = None
        self._parserFinished = False

    @staticmethod
    def _initDirectories():
        for directory in g_settingsConfig.Directories:
            try:
                FileSystem.makeDir(directory)
                _log.debug(f"Directory: <{directory}> created")
            except PathExistsException:
                _log.error(f"Directory: <{directory}> was not created")

    def run(self):
        self._initDirectories()
        self._initUI()
        if not self._checkPricesFile():
            _log.error("Price file does not exist")
            self._window.changeContext(LoadingContext)
            self._startThreads()
        self._runUI()

    @staticmethod
    def _checkPricesFile():
        return FileSystem.exists(g_settingsConfig.Data["pricesFile"])

    def _runParser(self):
        return Parser.run()

    def _startThreads(self):
        self._parserThread = threading.Thread(target=self._runParserThread)
        self._parserThread.start()
        barThread = threading.Thread(target=self._runBarThread)
        barThread.start()

    def _runParserThread(self):
        if self._runParser():
            _log.debug("Prices file created")
        else:
            _log.debug("Prices file was not created")
        self._parserFinished = True

    def _runBarThread(self):
        progress = 0
        while not self._parserFinished:
            while progress < 0.8 and not self._parserFinished:
                progress += 0.015
                time.sleep(0.5)
                self._window.context.updateProgress(progress)
            time.sleep(0.5)

        self._window.context.complete()
        self._window.changeContext(MainContext)

    def _initUI(self):
        self._window = MainWindow()

    def _runUI(self):
        self._window.mainloop()

import threading

from parser.parser import Parser
from settingsConfig import g_settingsConfig
from tools.fileSystem import FileSystem
from tools.fileSystemExceptions import PathExistsException
from tools.logger import logger
from ui.windows import MainWindow
from ui.contexts.loadingContext import LoadingContext


_log = logger.getLogger(__name__)


class App:
    def __init__(self):
        self._window = None

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
            self._startParserThread()
        self._runUI()

    @staticmethod
    def _checkPricesFile():
        return FileSystem.exists(g_settingsConfig.Data["pricesFile"])

    def _startParserThread(self):
        parserThread = threading.Thread(target=self._runParserThread)
        parserThread.start()

    def _runParserThread(self):
        if Parser.run():
            _log.debug("Prices file created")
            self._window.context.complete()
        else:
            _log.debug("Prices file was not created")

    def _initUI(self):
        self._window = MainWindow()

    def _runUI(self):
        self._window.mainloop()

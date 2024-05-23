import json
import threading

from parser.parser import Parser
from settingsConfig import g_settingsConfig
from tools.fileSystem import FileSystem
from tools.fileSystemExceptions import PathExistsException
from tools.logger import logger
from ui.windows import MainWindow


_log = logger.getLogger(__name__)


class App:
    def __init__(self):
        ...

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
        if not self._checkPricesFile():
            _log.error("Price file does not exist")
            parser_thread = threading.Thread(target=self._runParserThread)
            parser_thread.start()
            parser_thread.join()

        self._runUI()

    @staticmethod
    def _checkPricesFile():
        return FileSystem.exists(g_settingsConfig.Data["pricesFile"])

    @staticmethod
    def _runParser():
        if not Parser.run():
            return False
        return True

    def _runParserThread(self):
        if self._runParser():
            _log.debug("Prices file created")
        else:
            _log.debug("Prices file was not created")

    def _runUI(self):
        self._window = MainWindow()
        self._window.mainloop()

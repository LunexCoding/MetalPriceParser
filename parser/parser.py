from .driver import Browser
from .consts import SELECTORS, DRIVER_TYPES, Constants

from tools.logger import logger
from tools.convert import convertStringToNumber
from storage import g_storage


_log = logger.getLogger(__name__)


class Parser:
    @classmethod
    def run(cls):
        try:
            data = cls._getData()
            cls._saveData(data)
            return True
        except Exception as e:
            _log.error(e, exc_info=True)
            return False

    @staticmethod
    def _getData():
        browser = Browser(DRIVER_TYPES.FIREFOX)

        try:
            data = []

            browser.openUrl("https://nsk-metall54.ru/")

            table = browser.findElement(SELECTORS.TABLE)
            if table is None:
                return None

            rows = browser.findElement(SELECTORS.ROWS, element=table, all=True)
            if rows is None:
                return None
            # del headers
            del rows[0]
            del rows[0]

            for row in rows:
                if row is not None:
                    rowData = browser.findElement(SELECTORS.ROW_DATA, element=row, all=True)
                    if rowData is not None:
                        rowDataText = [item.text.replace("­", "") for item in rowData]
                        if len(rowDataText) == 3:
                            data.append(
                                {
                                    Constants.ITEM_NAME: rowDataText[0],
                                    Constants.ITEM_PRICE: convertStringToNumber(rowDataText[2])
                                }
                            )

            return data

        except Exception as e:
            _log.error(e, exc_info=True)
        finally:
            browser.close()

    @staticmethod
    def _saveData(data):
        g_storage.init(data)
        g_storage.writeData()

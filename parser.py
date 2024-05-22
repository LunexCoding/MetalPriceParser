from driver import Browser
from consts import SELECTORS, DRIVER_TYPES, Constants
from tools.logger import logger


_log = logger.getLogger(__name__)


if __name__ == "__main__":
    data = []

    browser = Browser(DRIVER_TYPES.FIREFOX)
    browser.openUrl("https://nsk-metall54.ru/")
    try:
        table = browser.findElement(SELECTORS.TABLE)
        rows = browser.findElement(SELECTORS.ROWS, element=table, all=True)
        del rows[0]
        del rows[0]

        for row in rows:
            rowData = browser.findElement(SELECTORS.ROW_DATA, element=row, all=True)
            rowDataText = [item.text.replace("­", "") for item in rowData]
            if len(rowDataText) == 3:
                data.append(
                    {
                        Constants.ITEM_NAME: rowDataText[0],
                        Constants.ITEM_PRICE: int(rowDataText[2])
                    }
                )

    except Exception as e:
        _log.error(e, exc_info=True)
    finally:
        browser.close()

    for item in data:
        print(item)

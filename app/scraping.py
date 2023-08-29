from app.domain.schedule import Item, ItemType, TournamentName, Date, Venue, SeatType, Note
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from typing import Optional

SELENIUM_URL = "http://chrome:4444"


class Scraping:
    def __init__(self):
        # Seleniumが起動しているか確認
        response = requests.get(SELENIUM_URL + "/wd/hub/status")
        if not response.ok or not response.json()["value"]["ready"]:
            raise Exception("Selenium is not ready. url: " +
                            SELENIUM_URL + "/wd/hub/status")

    def scrape_twitter(self, url: str) -> Optional[str]:
        """ 試合詳細を取得 """
        driver = self.__get_driver()
        try:
            driver.get(url)
            driver.implicitly_wait(5)
            elements = driver.find_elements(
                By.TAG_NAME, "meta")
            for element in elements:
                attribute = element.get_attribute('outerHTML')
                property = element.get_attribute('property')
                if "property" in attribute and "og:description" in property:
                    content = element.get_attribute('content')
                    return content
            return None
        finally:
            driver.quit()

    @staticmethod
    def __get_driver():
        """ Seleniumのドライバーを取得 """
        return webdriver.Remote(
            command_executor=SELENIUM_URL,
            options=webdriver.ChromeOptions()
        )


if __name__ == "__main__":
    # python -m app.scraping
    scraping = Scraping()
    result = scraping.scrape_twitter(
        "https://twitter.com/MLBear2/status/1696240260399906862")
    print(f"result: {result}")

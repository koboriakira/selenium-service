from app.domain.schedule import Item, ItemType, TournamentName, Date, Venue, SeatType, Note
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

SELENIUM_URL = os.environ.get("SELENIUM_URL", "http://localhost:4444")


class Scraping:
    def __init__(self):
        # Seleniumが起動しているか確認
        response = requests.get(SELENIUM_URL + "/wd/hub/status")
        if not response.ok or not response.json()["value"]["ready"]:
            raise Exception("Selenium is not ready. url: " +
                            SELENIUM_URL + "/wd/hub/status")

    def scrape(self, url: str):
        """ 試合詳細を取得 """
        driver = self.__get_driver()
        try:
            driver.implicitly_wait(2)
            driver.get(url)
            elements = driver.find_elements(
                By.CLASS_NAME, "Article_Table__item")
            print(elements)
            return elements
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
    # python -m tjpw_schedule.scraping
    scraping = Scraping()
    scraping.scrape("https://twitter.com/MLBear2/status/1696240260399906862")

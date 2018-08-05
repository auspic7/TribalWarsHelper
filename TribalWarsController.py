from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup


class TribalWarsController:
    driver = webdriver.Chrome('./chromedriver')
    MY_VILLAGE_URL = 'https://en102.tribalwars.net/game.php?village=30014&screen=overview'

    def check_login_session(self):
        self.driver.get("https://www.tribalwars.net/en-dk/")

        try:
            world_button = self.driver.find_element_by_xpath(
                '//*[@id="home"]/div[3]/div[3]/div[10]/div[3]/div[2]/div[1]/a/span')
        except NoSuchElementException:
            return False

        world_button.click()
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        username = soup.select('#menu_row > td:nth-of-type(11) > table > tbody > tr:nth-of-type(1) > td > a')[0].text

        if not username:
            return False
        else:
            return username

    def login(self, username, password):
        name = self.check_login_session()
        if name:
            return name

        self.driver.get("https://www.tribalwars.net/en-dk/")

        self.driver.find_element_by_xpath('//*[@id="user"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="login_form"]/div/div/a').click()

        WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element((By.XPATH, '//*[@id="login_form"]/div/div/a'), '...'))

        return self.check_login_session()

import sys
import requests
from selenium import webdriver
from PyQt5.QtWidgets import *
from PyQt5 import uic

driver = webdriver.Chrome('./chromedriver')
form_class = uic.loadUiType("mainwindow.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.login_button_slot)

    def login_button_slot(self):
        print("Login Button Clicked.")
        driver.get("https://www.tribalwars.net/en-dk/")

        driver.find_element_by_xpath('//*[@id="user"]').send_keys(self.usernameLine.text())
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.passwordLine.text())

        driver.find_element_by_xpath('//*[@id="login_form"]/div/div/a').click()
        driver.find_element_by_xpath('//*[@id="home"]/div[3]/div[3]/div[10]/div[3]/div[2]/div[1]/a/span').click()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

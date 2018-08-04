import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from TribalWarsController import TribalWarsController

form_class = uic.loadUiType("mainwindow.ui")[0]
helper = TribalWarsController()

class MyWindow(QMainWindow, form_class):
    isLootAssistantOn = False
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.login_button_slot)

    def login_button_slot(self):
        print("Login Button Clicked.")
        print(helper.login(self.usernameLine.text(), self.passwordLine.text()))

    def auto_loot_assistant_slot(self):
        self.isLootAssistantOn = ~self.isLootAssistantOn
        print("Auto loot assistant ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

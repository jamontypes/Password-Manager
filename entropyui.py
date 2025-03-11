'''
by : sam juarez
COLORS:
Textboxs - #F5F5F5
Text - #1A5319
Text (alt) - #80AF81

pages for:
logging in - done
viewing passwords - in progress
editing passwords - not started
adding passwords - not started
'''

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit
from PySide6.QtCore import Qt
import sys

#main log in window - sends to password manager
class LogInWindow(QWidget):
    def __init__(self):
        super().__init__()

        #main window set up
        self.setWindowTitle("Log In")
        self.setGeometry(100, 100, 900, 700)
        self.setStyleSheet("background-color: white;")

        #main layout creation - spacing between label and input while centered
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(10)

        #adds "enter password" text with style sheets
        login_label = QLabel("Enter Password...", self)
        login_label.setStyleSheet("font-size: 18px; color: black;")
        login_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(login_label)

        #password input box - all attributes
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("MAX 15 CHARS")
        self.password_input.setStyleSheet("""QLineEdit { background-color: #F5F5F5; color: #80AF81 }""")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMaxLength(15)
        self.password_input.setMaximumWidth(125)
        self.password_input.returnPressed.connect(self.PasswordValid)
        layout.addWidget(self.password_input)

    #checks if the password is valid "entropy"
    #opens passwordmanager window
    def PasswordValid(self):
        if self.password_input.text() != "entropy":
            print("wrong")
        else:
            self.password_manager = PasswordManager()
            self.password_manager.show()


#actual password manager window
class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()

        # Main window setup
        self.setWindowTitle("Password Manager")
        self.setGeometry(100, 100, 900, 700)
        self.setStyleSheet("background-color: white;")

    #code execution
if __name__ == "__main__":

    app = QApplication(sys.argv)
    login_window = LogInWindow()
    login_window.show()

    sys.exit(app.exec())

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QWidget, QSpacerItem, QSizePolicy, QLineEdit, QLabel
from src.gui.buttons.LoginButton import LoginButton
from src.gui.static.style import login_input_style, login_alert_label_style


class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.is_login = False
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)

        # ID input
        self.id_input = QLineEdit()
        self.id_input.setStyleSheet(login_input_style)
        self.id_input.setPlaceholderText("Enter your ID")
        self.id_input.textChanged.connect(self.clear_alert_label)  # Connect textChanged signal to clear_alert_label slot

        # Password input
        self.pw_input = QLineEdit()
        self.pw_input.setStyleSheet(login_input_style)
        self.pw_input.setPlaceholderText("Enter your PASSWORD")
        self.pw_input.setEchoMode(QLineEdit.Password)  # Hide password input
        self.pw_input.textChanged.connect(self.clear_alert_label)  # Connect textChanged signal to clear_alert_label slot

        # Password alert label
        self.alert_pw_label = QLabel()
        self.alert_pw_label.setStyleSheet(login_alert_label_style)
        self.alert_pw_label.setFixedHeight(20)

        # Login button
        self.button = LoginButton("Login")
        self.button.setFixedWidth(100)
        self.button.setFixedHeight(35)
        self.button.setCursor(Qt.PointingHandCursor)

        # Layout setting
        self.login_layout = QVBoxLayout()
        self.login_layout.addWidget(self.id_input)
        self.login_layout.addWidget(self.pw_input)
        self.login_layout.addWidget(self.alert_pw_label, alignment=Qt.AlignCenter)
        self.login_layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.login_layout)

    def clear_alert_label(self):
        self.alert_pw_label.clear()

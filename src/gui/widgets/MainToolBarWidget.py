from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QHBoxLayout, QLabel
from src.gui.buttons.CloseButton import CloseButton
from src.gui.buttons.MinimizeButton import MinimizeButton
from src.gui.static.style import main_title_style, main_logo_style


class MainToolBarWidget(QHBoxLayout):
    def __init__(self):
        super().__init__()

        # widget initialization
        self.setSpacing(0)
        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap(r"logo.png"))

        self.title_label = QLabel("")
        self.close_button = CloseButton("X")
        self.minimize_button = MinimizeButton("-")

        # widget style setting
        self.logo_label.setFixedSize(30, 30)
        self.logo_label.setStyleSheet(main_logo_style)
        self.title_label.setStyleSheet(main_title_style)
        self.close_button.setFixedSize(30, 30)
        self.minimize_button.setFixedSize(30, 30)

        # Layout setting
        self.addWidget(self.logo_label)
        self.addWidget(self.title_label)
        self.addWidget(self.minimize_button)
        self.addWidget(self.close_button)
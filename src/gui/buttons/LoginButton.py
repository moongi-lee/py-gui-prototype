from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QEvent, Qt
from src.gui.static.style import button_style, button_style_hover


class LoginButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(button_style)
        self.setCursor(Qt.PointingHandCursor)

    def enterEvent(self, event: QEvent) -> None:
        self.setStyleSheet(button_style_hover)

    def leaveEvent(self, event: QEvent) -> None:
        self.setStyleSheet(button_style)
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QEvent, Qt
from src.gui.static.style import toolbar_button_style, toolbar_button_style_close_hover


class CloseButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(toolbar_button_style)
        self.setCursor(Qt.PointingHandCursor)

    def enterEvent(self, event: QEvent) -> None:
        self.setStyleSheet(toolbar_button_style_close_hover)

    def leaveEvent(self, event: QEvent) -> None:
        self.setStyleSheet(toolbar_button_style)
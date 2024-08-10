from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QEvent, Qt
from src.gui.static.style import start_button_style_hover, start_button_style


class StartButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(start_button_style)
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedSize(135, 50)

    def enterEvent(self, event: QEvent) -> None:
        self.setStyleSheet(start_button_style_hover)

    def leaveEvent(self, event: QEvent) -> None:
        self.setStyleSheet(start_button_style)
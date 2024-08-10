from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QEvent, Qt
from src.gui.static.style import stop_button_style_hover, stop_button_style

class StopButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(stop_button_style)
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedSize(135, 50)

    def enterEvent(self, event: QEvent) -> None:
        self.setStyleSheet(stop_button_style_hover)

    def leaveEvent(self, event: QEvent) -> None:
        self.setStyleSheet(stop_button_style)
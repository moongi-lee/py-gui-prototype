from PySide6.QtWidgets import QApplication
from src.PrototypeWindow import PrototypeWindow

class IveTicketing(PrototypeWindow):
    def __init__(self):
        super().__init__()
        # 기본 설정
        self.toolbar_layout.title_label.setText("MG Ptotorype")
        self.setFixedSize(300, 250)
        self.resizable = True

if __name__ == '__main__':
    app = QApplication()
    window = IveTicketing()
    window.show()
    app.exec()


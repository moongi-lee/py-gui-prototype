from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainterPath, QRegion, QPainter, QPaintEvent
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QStackedLayout
from src.gui.widgets.ContentsWidget import ContentsWidget
from src.gui.widgets.LoginWidget import LoginWidget
from src.gui.widgets.MainToolBarWidget import MainToolBarWidget
from src.gui.static.style import main_layout_style

class PrototypeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 기본 데이터
        self.id = "admin"
        self.pw = "123123"
        self.oldPos = None

        # 스타일 설정
        self.setFixedSize(600, 400)
        self.resizable = True
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(main_layout_style)

        # 컨텐츠 레이아웃
        self.window_layout = QVBoxLayout()
        self.window_layout.setContentsMargins(0, 0, 0, 0)
        self.window_layout.setSpacing(0)

        ## 프레임 레이아웃
        self.toolbar_layout = MainToolBarWidget()
        self.toolbar_layout.minimize_button.clicked.connect(self.minimize_window)
        self.toolbar_layout.close_button.clicked.connect(self.close_window)
        self.toolbar_layout.setContentsMargins(0, 0, 0, 0)

        ## 위젯 불러오기
        self.login_widget = LoginWidget()
        self.login_widget.setStyleSheet("margin: 0px; padding: 0px;")
        self.login_widget.button.clicked.connect(self.login_allow)
        self.contents_widget = ContentsWidget()
        self.contents_widget.setStyleSheet("margin: 0px; padding: 0px;")

        ## 내용 레이아웃
        self.main_layout = QStackedLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.login_widget)
        self.main_layout.addWidget(self.contents_widget)
        self.main_layout.setCurrentIndex(0)

        ## 레이아웃 배치
        self.window_layout.addLayout(self.toolbar_layout)
        self.window_layout.addLayout(self.main_layout)

        # 윈도우 설정
        widget = QWidget()
        widget.setLayout(self.window_layout)
        self.setCentralWidget(widget)

    # 윈도우 최소화, 닫기
    def minimize_window(self):
        self.showMinimized()

    def close_window(self):
        self.close()

    # 로그인 함수
    def login_allow(self):
        if self.login_widget.id_input.text() != self.id or self.login_widget.pw_input.text() != self.pw:
            self.login_widget.alert_pw_label.setText("아이디 혹은 비밀번호가 틀렸습니다.")
        else:
            self.main_layout.setCurrentIndex(1)
            self.login_widget.is_login = True

    # 드레그 이벤트 함수
    def mousePressEvent(self, event):
        # Check if the mouse click occurred within the geometry of top_layout
        if self.toolbar_layout.geometry().contains(event.pos()):
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        # Check if oldPos is not None, which means a mouse press event occurred within top_layout
        if self.oldPos is not None:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        # Reset oldPos to None when the mouse is released
        self.oldPos = None

    # 모서리 둥글게
    # def resizeEvent(self, event):
    #     path = QPainterPath()
    #     path.addRoundedRect(self.rect(), 10, 10)
    #     self.setMask(QRegion(path.toFillPolygon().toPolygon()))
    #     super().resizeEvent(event)

    # 모서리 둥글게
    def paintEvent(self, event: QPaintEvent) -> None:
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 계단현상 방지
        path = QPainterPath()
        path.addRoundedRect(self.rect(), 10, 10)
        painter.fillPath(path, Qt.white)  # 배경색으로 채우기

        # 창 내용 그리기 (QPainter를 사용하여 각 위젯을 직접 그리기)
        painter.translate(self.rect().topLeft())
        for i in range(self.window_layout.count()):
            item = self.window_layout.itemAt(i)
            if item.widget():
                item.widget().render(painter, item.widget().rect().topLeft())

                # 윈도우 모양 제한
        self.setMask(QRegion(path.toFillPolygon().toPolygon()))
from PySide6.QtCore import Slot
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QTextEdit, QLineEdit, QApplication
from src.gui.buttons.StartButton import StartButton
from src.gui.buttons.StopButton import StopButton
from src.gui.static.style import log_board_style, login_input_style
from datetime import datetime
import keyboard
import pyautogui
import multiprocessing


multiprocessing.set_start_method('spawn', force=True)


class ContentsWidget(QWidget):
    def __init__(self):
        super().__init__()


        # multiprocessing
        self.process = None

        # initialize layout
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)  # Remove default margin and padding
        self.input_layout = QHBoxLayout()
        self.log_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()

        # input widget
        self.xpoint_input = QLineEdit()
        self.xpoint_input.setStyleSheet(login_input_style)
        self.xpoint_input.setPlaceholderText("x-p")
        self.ypoint_input = QLineEdit()
        self.ypoint_input.setStyleSheet(login_input_style)
        self.ypoint_input.setPlaceholderText("y-p")
        self.ms_value = QLineEdit()
        self.ms_value.setStyleSheet(login_input_style)
        self.ms_value.setPlaceholderText("ms-v")
        self.target_time = QLineEdit()
        self.target_time.setStyleSheet(login_input_style)
        self.target_time.setPlaceholderText("target")
        self.input_layout.addWidget(self.xpoint_input)
        self.input_layout.addWidget(self.ypoint_input)
        self.input_layout.addWidget(self.target_time)
        self.input_layout.addWidget(self.ms_value)


        # left, top, right, bottom
        self.button_layout.setContentsMargins(10, 5, 10, 10)

        # initialize widgets
        self.log_board = QTextEdit()
        self.log_board.setReadOnly(True)
        self.start_button = StartButton("Start")
        # self.start_button.clicked.connect(self.start_button_clicked)
        self.start_button.clicked.connect(self.start_button_clicked)
        self.stop_button = StopButton("Stop")
        self.stop_button.clicked.connect(self.stop_button_clicked)

        # set widget style
        self.log_board.setStyleSheet(log_board_style)

        # set layout
        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addWidget(self.log_board)
        self.main_layout.addLayout(self.button_layout)
        self.button_layout.addWidget(self.start_button)
        self.button_layout.addWidget(self.stop_button)
        self.setLayout(self.main_layout)

        # set shortcut
        keyboard.add_hotkey('ctrl+x', self.copy_coordinates)
        # keyboard.add_hotkey('ctrl+c', self.stop_process)

    def copy_coordinates(self):
        # 현재 마우스 좌표 가져오기
        cursor = QCursor()
        x = cursor.pos().x()
        y = cursor.pos().y()

        # QLineEdit에 좌표 입력
        self.xpoint_input.setText(str(x))
        self.ypoint_input.setText(str(y))

    def stop_button_clicked(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.log_board.append(f"{now} - 작업종료")
        quit()

    def start_button_clicked(self):
        x_point = None
        y_point = None
        target_time = None
        ms_range = None
        try:
            x_point = int(self.xpoint_input.text())
            y_point = int(self.ypoint_input.text())
            target_time = int(self.target_time.text())
            ms_range = int(self.ms_value.text())
        except ValueError:
            self.log_board.append("입력값을 모두 입력해주세요.")
            return

        # self.log_board.append("서버 타임존 값 로드중")
        # QApplication.processEvents()
        # user_agents = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        # url = "https://cafe.daum.net"
        # headers = {
        #     'User-Agent': user_agents
        # }

        # response = requests.get(url, headers=headers)
        # self.log_board.append("서버 타임존 값 세팅")
        # QApplication.processEvents()
        # date_str = response.headers.get('Date')
        # self.log_board.append(f"서버 타임존 값 {date_str}")
        # QApplication.processEvents()
        #
        # self.log_board.append("3초뒤 작업을 시작합니다.")
        # time.sleep(1)
        # QApplication.processEvents()
        # self.log_board.append("2초뒤 작업을 시작합니다.")
        # time.sleep(1)
        # QApplication.processEvents()
        # self.log_board.append("1초뒤 작업을 시작합니다.")
        # time.sleep(1)
        # QApplication.processEvents()

        now = datetime.now().strftime("%H:%M:%S")
        self.log_board.append(f"{now} - 작업시작")
        # time.sleep(0.5)
        # target time = 분
        # ms_range = 밀리세컨드 범위  850 860  추천값
        # x_point, y_point = 클릭할 좌표
        while True:
            now = datetime.now()
            self.log_board.append(f"대기중 : {now.strftime('%M:%S.%f')[:-3]}")
            min = int(now.strftime('%M'))
            sec = int(now.strftime('%S'))
            ms_sceond = int(now.strftime('%f')[:-3])
            if min == target_time:
                if sec == 0:
                    if ms_range < ms_sceond < ms_range + 100:
                        pyautogui.click(x_point, y_point)
                        self.log_board.append("작업 완료")
                        break
            QApplication.processEvents()

    # @Slot()
    # def start_process(self):
    #     if self.process is None or not self.process.is_alive():
    #         self.process = multiprocessing.Process(target=start_traffic)
    #         self.process.start()
    #         # self.process = subprocess.Popen(['python', 'my_worker.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
    #
    # @Slot()
    # def stop_process(self):
    #     if self.process is not None and self.process.is_alive():
    #         self.process.terminate()
    #         self.process.join()
    #         self.process = None
    #         WindowEngine.clean_process()

    # @staticmethod
    # def worker():
    #     signal.signal(signal.SIGINT, signal.SIG_IGN)  # Ignore interrupt signal in worker
    #     while True:
    #         print("작업 중...")
    #         time.sleep(1)
    #
    # @staticmethod
    # def start_traffic():
    #     starter = SeleniumStarter()
    #     starter.start_work()


import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from widgets.canvas_widget import CanvasWidget
from config import get_config

from libs.version import __version__

__appname__ = 'Image Viewer'
form_class = uic.loadUiType("UI/image_viewer_main.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._initData()
        self._loadUiInit()
        self._setEvent()


    def _initData(self):
        '''
        Data 초기화
        :return:
        '''
        self._config = get_config()
        pass


    def _loadUiInit(self):
        '''
        UI 초기화
        :return: None
        '''
        self.setWindowTitle("{title} ({version})".format(title=__appname__, version=__version__))
        self.canvas_widget = CanvasWidget()
        self.layout_canvas.addWidget(self.canvas_widget)
        pass


    def _setEvent(self):
        '''
        Event 설정
        :return: None
        '''
        self.action_openFile.triggered.connect(self.openFile)            # 메뉴 - Open File
        pass


    def openFile(self):
        if self._config["debug"]:
            print('Debug : Open File')

        QMessageBox.information(self, "Open File", "Open file event")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    exit(app.exec_())
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

parentDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
widget_class = uic.loadUiType(os.path.join(parentDir, "UI/canvas_widget.ui"))[0]

class CanvasWidget(QWidget, widget_class):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._loadUiInit()
        self._setEvent()

    def _loadUiInit(self):
        '''
        UI 초기화
        :return: None
        '''
        pass


    def _setEvent(self):
        '''
        Event 설정
        :return: None
        '''
        pass

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    canvas_widget = CanvasWidget()
    canvas_widget.show()
    exit(app.exec_())
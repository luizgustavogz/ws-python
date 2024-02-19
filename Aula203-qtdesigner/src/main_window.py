from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
from window import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.buttonSend.clicked.connect(self.updateLabelResult)

    def updateLabelResult(self):
        text = self.lineName.text()
        self.labelResult.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()

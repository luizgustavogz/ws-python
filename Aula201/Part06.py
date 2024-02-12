# Trabalhando com classes e herança no PySide6
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget,
                               QGridLayout, QMainWindow)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Aula 201')

        # Botão
        self.btn = self.make_button('Hello World')
        self.btn.clicked.connect(self.action_check)

        self.btn2 = self.make_button('Confirm')

        self.btn3 = self.make_button('Cancel')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.btn, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.btn2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.btn3, 3, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Status Bar')

        # menuBar
        self.menu_bar = self.menuBar()
        self.menu = self.menu_bar.addMenu('First menu')
        self.action = self.menu.addAction('First action')
        self.action.triggered.connect(self.change_status_bar_message)

        self.action2 = self.menu.addAction('Second action')
        self.action2.setCheckable(True)
        self.action2.toggled.connect(self.action_check)
        self.action2.hovered.connect(self.action_check)

    @Slot()
    def change_status_bar_message(self):
        self.status_bar.showMessage('Slot executed')

    @Slot()
    def action_check(self):
        print('Is checked?', self.action2.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 80px;')
        return btn


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()
    app.exec()

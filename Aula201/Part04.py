# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (btn)
#               -> Widget 2 (btn2)
#               -> Widget 3 (btn3)
#   -> show
# -> exec
import sys

from PySide6.QtWidgets import (QApplication, QPushButton, QWidget,
                               QGridLayout, QMainWindow)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle("Aula 201")

btn = QPushButton("Hello World")
btn.setStyleSheet('font-size: 80px;')

btn2 = QPushButton("Confirmar")
btn2.setStyleSheet('font-size: 40px;')

btn3 = QPushButton("Cancelar")
btn3.setStyleSheet('font-size: 40px;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(btn, 1, 1, 1, 1)
layout.addWidget(btn2, 1, 2, 1, 1)
layout.addWidget(btn3, 3, 1, 1, 2)


def slot_example(status_bar):
    status_bar.showMessage("Slot executado")


# statusBar
status_bar = window.statusBar()
status_bar.showMessage("Status Bar")

# menuBar
menu_bar = window.menuBar()
menu = menu_bar.addMenu("Primeiro menu")
action = menu.addAction("Primeira ação")
action.triggered.connect(lambda: slot_example(status_bar))


window.show()
app.exec()  # O loop da aplicação

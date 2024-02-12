# O básico sobre Signal e Slots (eventos e documentação)
import sys

from PySide6.QtCore import Slot
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


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage("Slot executado")
    return inner


@Slot()
def slot_example2(checked):
    print('Está marcado?', checked)


@Slot()
def slot_example3(action):
    def inner():
        slot_example2(action.isChecked())
    return inner


# statusBar
status_bar = window.statusBar()
status_bar.showMessage("Status Bar")

# menuBar
menu_bar = window.menuBar()
menu = menu_bar.addMenu("Primeiro menu")
action = menu.addAction("Primeira ação")
action.triggered.connect(slot_example(status_bar))

action2 = menu.addAction("Segunda ação")
action2.setCheckable(True)
action2.toggled.connect(slot_example2)
action2.hovered.connect(slot_example3(action2))

btn.clicked.connect(slot_example3(action2))

window.show()
app.exec()  # O loop da aplicação

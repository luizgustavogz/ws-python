# QWidget e QLayout de PySide6.QtWidgets
# - QWidget -> Classe genérica/base para todos os widgets
# - QLayout -> Um Widget de layout que recebe outros widgets
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)

btn = QPushButton("Hello World")
btn.setStyleSheet('font-size: 80px;')

btn2 = QPushButton("Confirmar")
btn2.setStyleSheet('font-size: 40px;')

btn3 = QPushButton("Cancelar")
btn3.setStyleSheet('font-size: 40px;')

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(btn, 1, 1, 1, 1)  # row, column, rowspan, colspan
layout.addWidget(btn2, 1, 2)  # deafult rowspan=1, colspan=1
layout.addWidget(btn3, 3, 1, 1, 2)  # colspan=2 para ocupar 2 colunas

central_widget.show()  # Central widget entre na hierarquia e mostre sua janela
app.exec()  # O loop da aplicação

import qdarktheme
import re

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget, QLineEdit,
                               QLabel, QPushButton, QGridLayout)

from variables import (BIG_FONT_SIZE, MEDIUM_FONT_SIZE, SMALL_FONT_SIZE,
                       TEXT_MARGIN, MINIMUM_WIDTH, PRIMARY_COLOR,
                       DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR)


# Classe da janela principal
class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Título da janela
        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self) -> None:
        # Última coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget) -> None:
        self.vLayout.addWidget(widget)

    def addLayoutToVLayout(self, widget: QGridLayout) -> None:
        self.vLayout.addLayout(widget)


# Classe de display (tela da calculadora)
class Display(QLineEdit):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self) -> None:
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])


# Classe de informações (acima do display)
class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self) -> None:
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)


# Classe de botão
class Button(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self) -> None:
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


# Classe de grid de botões
class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '='],
        ]
        self._makeGrid()

    def _makeGrid(self) -> None:
        for rowNum, rowData in enumerate(self._gridMask):
            for columnNum, buttonText in enumerate(rowData):
                if buttonText:
                    button = Button(buttonText)
                    button.setText(self._gridMask[rowNum][columnNum])

                    if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                        button.setProperty('cssClass', 'specialButton')

                    if buttonText == '0':
                        self.addWidget(button, rowNum, columnNum, 1, 2)
                    else:
                        self.addWidget(button, rowNum, columnNum)


# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
# Styles - Dark Theme
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setupTheme() -> None:
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}",
            },
        },
        additional_qss=qss
    )


# Functions - Utils
NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(string: str) -> bool:
    return bool(NUM_OR_DOT_REGEX.search(string))


def isEmpty(string: str) -> bool:
    return len(string) == 0

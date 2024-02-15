import qdarktheme
import re

from PySide6.QtCore import Qt, Slot
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
    def __init__(self, display: Display, info: Info, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self._equationInitialValue = 'Sua conta'
        self._leftNum = None
        self._rightNum = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self) -> str:
        return self._equation

    @equation.setter
    def equation(self, value) -> None:
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self) -> None:
        for rowNum, rowData in enumerate(self._gridMask):
            for columnNum, btnText in enumerate(rowData):
                if btnText == '':
                    continue

                if not btnText == '0':
                    btn = Button(btnText)

                    if not isNumOrDot(btnText):
                        btn.setProperty('cssClass', 'specialButton')
                        self._configSpecialButton(btn)

                    self.addWidget(btn, rowNum, columnNum)

                    slot = self._makeSlot(self._insertButtonTextToDisplay, btn)
                    self._connectButtonClicked(btn, slot)
                else:
                    btn0 = Button(btnText)
                    self.addWidget(btn0, rowNum, columnNum, 1, 2)

                    slot0 = self._makeSlot(
                        self._insertButtonTextToDisplay, btn0)
                    self._connectButtonClicked(btn0, slot0)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text in '+-/*':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._operatorClicked, button)
            )

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)

    def _clear(self):
        self._leftNum = None
        self._rightNum = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        btnText = button.text()  # Operador (+ - * /)
        displayText = self.display.text()  # Deverá ser _leftNum
        self.display.clear()  # Limpa o display

        # Se a pessoa clicou no operador sem ter digitado um número
        if not isValidNumber(displayText) and self._leftNum is None:
            return

        # Se _leftNum já foi definido, aguarda _rightNum
        if self._leftNum is None:
            self._leftNum = float(displayText)

        self._op = btnText
        self.equation = f'{self._leftNum} {self._op} ??'


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


def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


def isEmpty(string: str) -> bool:
    return len(string) == 0

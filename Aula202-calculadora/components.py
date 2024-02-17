import qdarktheme
import re
import math

from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget, QLineEdit,
                               QLabel, QPushButton, QGridLayout, QMessageBox)

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

    def makeMsgBox(self):
        return QMessageBox(self)


# Classe de display (tela da calculadora)
class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self) -> None:
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOperator = key in [
            KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Asterisk, KEYS.Key_Slash,
            KEYS.Key_P
        ]

        if isEnter:
            self.eqPressed.emit()
            return event.ignore()

        if isDelete:
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            self.clearPressed.emit()
            return event.ignore()

        if isOperator:
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()

        # Não passar daqui se não tiver texto
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()


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
    def __init__(
            self, display: Display, info: Info, window: MainWindow,
            *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N', '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
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
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for rowNum, rowData in enumerate(self._gridMask):
            for columnNum, btnText in enumerate(rowData):
                btn = Button(btnText)

                if not isNumOrDot(btnText) and not isEmpty(btnText):
                    btn.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(btn)

                self.addWidget(btn, rowNum, columnNum)
                slot = self._makeSlot(self._insertToDisplay, btnText)
                self._connectButtonClicked(btn, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text == '◀':
            self._connectButtonClicked(button, self.display.backspace)

        if text == 'N':
            self._connectButtonClicked(button, self._invertNumber)

        if text in '+-/*^':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._configLeftOp, text)
            )

        if text == '=':
            self._connectButtonClicked(button, self._eq)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        number = convertToNumber(displayText) * -1
        self.display.setText(str(number))
        self.display.setFocus()

    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self._leftNum = None
        self._rightNum = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _configLeftOp(self, text):
        displayText = self.display.text()  # Deverá ser _leftNum
        self.display.clear()  # Limpa o display
        self.display.setFocus()

        # Se a pessoa clicou no operador sem ter digitado um número
        if not isValidNumber(displayText) and self._leftNum is None:
            self._showError('Você não digitou nada.')
            return

        # Se _leftNum já foi definido, aguarda _rightNum
        if self._leftNum is None:
            self._leftNum = convertToNumber(displayText)

        self._op = text
        self.equation = f'{self._leftNum} {self._op} ??'

    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._leftNum is None:
            self._showError('Conta incompleta.')
            return

        self._rightNum = convertToNumber(displayText)
        self.equation = f'{self._leftNum} {self._op} {self._rightNum}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._leftNum, int | float):
                # result = eval(self.equation.replace('^', '**'))
                result = math.pow(self._leftNum, self._rightNum)
                result = convertToNumber(str(result))
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Divisão por zero.')
        except OverflowError:
            self._showError('Essa conta não pode ser realizada.')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._leftNum = result
        self._rightNum = None
        self.display.setFocus()

        if result == 'error':
            self._leftNum = None

    @Slot()
    def _backspace(self):        
        self.display.backspace()
        self.display.setFocus()

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setInformativeText('Clique em OK para continuar...')
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.setWindowTitle('Erro')
        msgBox.exec()
        self.display.setFocus()

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.setWindowTitle('Info')
        msgBox.exec()
        self.display.setFocus()

        # msgBox.setStandardButtons(
        #     msgBox.StandardButton.Ok |
        #     msgBox.StandardButton.Cancel |
        #     msgBox.StandardButton.Save
        # )

        # msgBox.button(msgBox.StandardButton.Cancel).setText('Cancelar')


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


def convertToNumber(string: str):
    num = float(string)

    if num.is_integer():
        num = int(num)

    return num


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

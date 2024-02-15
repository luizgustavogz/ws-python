import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from components import MainWindow, Display, Info, setupTheme, Button
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')

    # Info
    info = Info('2.0 ^ 10 = 1024')
    window.addToVLayout(info)

    # Display
    display = Display()
    window.addToVLayout(display)

    # Button
    button = Button('Texto do botão')
    window.addToVLayout(button)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()

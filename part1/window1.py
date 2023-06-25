from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

"""
QMainWindow: provides framework for base of app interface
-   Has related classes for main window mgmt, Also its own
    layout where you can add QToolBars, QDockWidgets, a QMenuBar
    and QStatusBar

"""

window = QMainWindow()
window.statusBar().showMessage("Message Example")
window.menuBar().addMenu("File")

window.show()

sys.exit(app.exec())

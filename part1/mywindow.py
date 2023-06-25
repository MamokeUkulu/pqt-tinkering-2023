from PyQt6.QtWidgets import QApplication, QWidget
import sys

# Only one per application
# Manages control flow
app = QApplication(sys.argv)

"""
QWidget: base class for all ui objects. Recieves mouse, keyboard
    and other events from the window system and paints a representation
    of itself on screen

"""

window = QWidget()

window.show()

sys.exit(app.exec())


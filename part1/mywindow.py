from PyQt6.QtWidgets import QApplication, QWidget
import sys

# Only one per application
# Manages control flow
app = QApplication(sys.argv)

# window types, Widget, MainWIndow, Dialog
window = QWidget()

window.show()

sys.exit(app.exec())
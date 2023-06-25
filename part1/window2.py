from PyQt6.QtWidgets import QApplication, QDialog
import sys

app = QApplication(sys.argv)

"""
QDialog: For shorterm tasks, & brief communication with the user
-    Can be  Modal or Modeless
    - Modal - require user to respond before continuing
    - Modeless - stay on the screen & are available for use
        at any time but permit other user activities

"""
window = QDialog()

window.show()

sys.exit(app.exec())

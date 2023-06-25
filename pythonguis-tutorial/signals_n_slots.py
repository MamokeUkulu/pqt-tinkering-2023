import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # track state within a widget by giving it instance
        # variables, this way, slots can access it
        self.button_is_checked = True

        self.setWindowTitle("Sparkly-Shiny")
        
        self.button = QPushButton("Press Me!")
        # makes this button togglable,so it provides a checked state
        self.button.setCheckable(True)
        self.button.setChecked(self.button_is_checked)
        # bind the the "clicked signal" (event) to a slot (listener)
        self.button.clicked.connect(self.the_button_was_clicked)

        # You can connect as many slots to a signal as you like and can respond to 
        # different versions of signals at the same time on your slots.
        # It is also possible to chain things using signals. Since
        # effects are decoupled from their triggers, subsequent effects
        # don't need to know ehat triggered them
        self.button.clicked.connect(self.the_button_was_toggled)

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    # This is what PyQt calls a "slot"
    # Basically an eveny listener? Or is there more?
    # Yes there is more:
    # Event is sent to the main loop, which then determines when
    #   it is delivered to the recieving side and what happens next
    #   - async, Order of execution not necessarily maintained
    #   - Think hardware, small and finite set
    #   - know nothing about widget context
    # Signal is executed in same thread of code as the 
    #   function that caused it, immedately after the function
    #   - sync, Order of execution maintained
    #   - Think widget-layer logic, arbitrarily complex & numerous
    #   - one signal can be fired due to different events
    #   - similar concept to "hooks"
    # https://stackoverflow.com/questions/9323888/what-are-the-differences-between-event-and-signal-in-qt
    def the_button_was_clicked(self):
        print("Clicked!")
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        # Also change the window title.
        self.setWindowTitle("My Oneshot App")

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print("Checked?", self.button_is_checked )


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
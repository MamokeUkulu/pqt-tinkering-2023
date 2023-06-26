from dataclasses import dataclass
import sys
import json
from typing import List, Optional
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QListView, QLineEdit, QWidget, QVBoxLayout)
from PyQt6.QtCore import Qt

import dbmodel

# qt_creator_file = "mainwindow.ui"
# MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)
tick = QtGui.QImage('tick.png')

@dataclass
class Todo:
    complete: bool
    text: str

# Model
class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, *args, todos: Optional[List[Todo]] = None, **kwargs):
        super(TodoModel, self).__init__(*args, **kwargs)
        self.todos: List[Todo] = todos or []
        
    def data(self, index, role):
        print(f"{index}, {role}")
        if role == Qt.ItemDataRole.DisplayRole:
            text = self.todos[index.row()].text
            return text
        
        if role == Qt.ItemDataRole.DecorationRole:
            status = self.todos[index.row()].complete
            if status:
                return tick

    def rowCount(self, index):
        return len(self.todos)

# View-Controller
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.model = TodoModel()
        self.load()

        self.todoView = QListView()
        self.todoEdit = QLineEdit()
        self.addButton = QPushButton("add")
        self.deleteButton = QPushButton("delete")
        self.completeButton = QPushButton("complete")

        layout = QVBoxLayout()
        layout.addWidget(self.todoView)
        layout.addWidget(self.todoEdit)
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addWidget(self.completeButton)

        container = QWidget()
        container.setLayout(layout)

        self.todoView.setModel(self.model)
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)

        self.setCentralWidget(container)


    def add(self):
        """
        Add an item to our todo list, getting the text from the QLineEdit .todoEdit
        and then clearing it.
        """
        text = self.todoEdit.text()
        if text: # Don't add empty strings.
            # Access the list via the model.
            self.model.todos.append(Todo(complete=False, text=text))
            # Trigger refresh.        
            self.model.layoutChanged.emit()
            # Empty the input
            self.todoEdit.setText("")
            self.save()
        
    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            # Indexes is a list of a single item in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
            self.save()
            
    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = Todo(True, text)
            # .dataChanged takes top-left and bottom right, which are equal 
            # for a single selection.
            self.model.dataChanged.emit(index, index)
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
            self.save()
    
    def load(self):
        try:
            self.model.todos = dbmodel.find_all()
            # with open('data.db', 'r') as f:
            #     self.model.todos = json.load(f)
        except Exception:
            pass

    # remove this and have the other functions interface with the db.
    def save(self):
        dbmodel.create_all(self.model.todos)
        # with open('data.db', 'w') as f:
        #     json.dump(self.model.todos, f)

dbmodel.build_tables()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


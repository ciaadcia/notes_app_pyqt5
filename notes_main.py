from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout
import json

app = QApplication([])

notes = {
    "Welcome!": {
        "text": "This is the best note taking app in the world!",
        "tags": ["good", "instructions"]
    }
}

with open("notes_data.json", "w") as file:
    json.dump(notes, file, ensure_ascii=False)

notes_win = QWidget()
notes_win.setWindowTitle("Smart Notes")
notes_win.resize(900, 600)

list_notes = QListWidget()
list_notes_label = QLabel("List of notes")

button_note_create = QPushButton("Create note")
button_note_del = QPushButton("Delete note")
button_note_save = QPushButton("Save note")

field_tag = QLineEdit()
field_tag.setPlaceholderText("Enter tag...")
field_text = QTextEdit()
button_add = QPushButton("Add to note")
button_del = QPushButton("Untag from note")
button_search = QPushButton("Search notes by tag")

list_tags = QListWidget()
list_tags_label = QLabel("List of tags")

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)

col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_3 = QHBoxLayout()
row_3.addWidget(button_add)
row_3.addWidget(button_del)

row_4 = QHBoxLayout()
row_4.addWidget(button_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, 2)
layout_notes.addLayout(col_2, 1)
notes_win.setLayout(layout_notes)

def show_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        field_text.setText(notes[key]["text"])
        list_tags.clear()
        list_tags.addItems(notes[key]["tags"])

list_notes.itemClicked.connect(show_note)

with open("notes_data.json", "r") as file:
    notes = json.load(file)

list_notes.addItems(notes.keys())

notes_win.show()
app.exec_()

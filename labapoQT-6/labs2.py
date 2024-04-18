import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QCalendarWidget, QTimeEdit, QListWidget, QListWidgetItem
from PyQt6.QtCore import QDateTime

class ReminderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Reminder App')


        layout = QVBoxLayout()

        #  widgets
        self.event_name_edit = QLineEdit()
        self.calendar = QCalendarWidget()
        self.time_edit = QTimeEdit()
        self.add_button = QPushButton('Add')
        self.event_list = QListWidget()


        layout.addWidget(self.event_name_edit)
        layout.addWidget(self.calendar)
        layout.addWidget(self.time_edit)
        layout.addWidget(self.add_button)
        layout.addWidget(self.event_list)


        self.setLayout(layout)


        self.add_button.clicked.connect(self.add_event)

    def add_event(self):
        event_name = self.event_name_edit.text()
        date = self.calendar.selectedDate()
        time = self.time_edit.time()

        if event_name:
            datetime = QDateTime(date, time)
            item = QListWidgetItem(datetime.toString("dd.MM.yyyy hh:mm") + " - " + event_name)
            self.event_list.addItem(item)
            self.event_list.sortItems()


            self.event_name_edit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ReminderApp()
    ex.show()
    sys.exit(app.exec())
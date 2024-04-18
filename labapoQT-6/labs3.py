import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget, QListWidgetItem

class AddressBook(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Address Book')


        layout = QVBoxLayout()


        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText('Enter contact name')
        self.phone_edit = QLineEdit()
        self.phone_edit.setPlaceholderText('Enter phone number')
        self.add_button = QPushButton('Add Contact')
        self.contact_list = QListWidget()


        layout.addWidget(self.name_edit)
        layout.addWidget(self.phone_edit)
        layout.addWidget(self.add_button)
        layout.addWidget(self.contact_list)

        self.setLayout(layout)


        self.add_button.clicked.connect(self.add_contact)

    def add_contact(self):
        name = self.name_edit.text()
        phone = self.phone_edit.text()

        if name and phone:
            item = QListWidgetItem(f"{name}: {phone}")
            self.contact_list.addItem(item)

            # Clear the input fields
            self.name_edit.clear()
            self.phone_edit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    address_book = AddressBook()
    address_book.show()
    sys.exit(app.exec())
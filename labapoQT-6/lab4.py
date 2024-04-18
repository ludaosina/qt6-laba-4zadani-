import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QLineEdit, QWidget, QMessageBox


class NimGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Игра "Псевдоним"')
        self.setGeometry(100, 100, 400, 300)
        widget = QWidget(self)
        self.setCentralWidget(widget)

        # Layout and widgets
        layout = QVBoxLayout()

        self.status_label = QLabel("Введите начальное количество камней и нажмите 'Начать игру':", self)
        layout.addWidget(self.status_label)

        self.stone_input = QLineEdit(self)
        layout.addWidget(self.stone_input)

        self.start_button = QPushButton('Начать игру', self)
        self.start_button.clicked.connect(self.start_game)
        layout.addWidget(self.start_button)

        self.pick_button1 = QPushButton('Взять 1 камень', self)
        self.pick_button1.clicked.connect(lambda: self.make_move(1))
        self.pick_button1.setEnabled(False)
        layout.addWidget(self.pick_button1)

        self.pick_button2 = QPushButton('Взять 2 камня', self)
        self.pick_button2.clicked.connect(lambda: self.make_move(2))
        self.pick_button2.setEnabled(False)
        layout.addWidget(self.pick_button2)

        self.pick_button3 = QPushButton('Взять 3 камня', self)
        self.pick_button3.clicked.connect(lambda: self.make_move(3))
        self.pick_button3.setEnabled(False)
        layout.addWidget(self.pick_button3)

        widget.setLayout(layout)

    def start_game(self):
        try:
            self.total_stones = int(self.stone_input.text())
            if self.total_stones <= 0:
                raise ValueError
            self.status_label.setText(f"Камней в куче: {self.total_stones}. Ваш ход!")
            self.enable_buttons()
        except ValueError:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите корректное число камней (целое число больше 0).')

    def enable_buttons(self):
        self.pick_button1.setEnabled(True)
        self.pick_button2.setEnabled(self.total_stones >= 2)
        self.pick_button3.setEnabled(self.total_stones >= 3)

    def make_move(self, stones):
        self.total_stones -= stones
        if self.total_stones <= 0:
            QMessageBox.information(self, 'Игра окончена', 'Поздравляем! Вы выиграли!')
            self.reset_game()
        else:
            self.status_label.setText(f"Камней в куче: {self.total_stones}. Ход компьютера...")
            self.computer_move()

    def computer_move(self):
        # Simple AI for example purposes
        stones = random.randint(1, min(self.total_stones, 3))
        self.total_stones -= stones
        if self.total_stones <= 0:
            QMessageBox.information(self, 'Игра окончена', 'К сожалению, вы проиграли.')
            self.reset_game()
        else:
            self.status_label.setText(f"Камней в куче: {self.total_stones}. Ваш ход!")
            self.enable_buttons()

    def reset_game(self):
        self.total_stones = 0
        self.pick_button1.setEnabled(False)
        self.pick_button2.setEnabled(False)
        self.pick_button3.setEnabled(False)
        self.status_label.setText("Игра окончена. Введите количество камней и нажмите 'Начать игру' для новой игры.")


def main():
    app = QApplication(sys.argv)
    ex = NimGame()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

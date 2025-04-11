import sys
import random, string, secrets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton,
    QVBoxLayout, QLineEdit, QLabel, QComboBox, QTextEdit, QMenu, QLayout,QDialog
)
from PyQt6.QtGui import (QAction)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        menu_bar=self.menuBar()

        file_menu=menu_bar.addMenu("File")

        tools_menu = menu_bar.addMenu("Tools")

        save_action=QAction("Save as txt",self)
        save_action.triggered.connect(self.save_txt)
        file_menu.addAction(save_action)

        exit_action=file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)

        clear_action=tools_menu.addAction("Clear")
        clear_action.triggered.connect(self.clear_input)

        self.input = QLineEdit()
        self.input.setPlaceholderText("size")
        self.input.setFixedWidth(200)
        self.input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.input, alignment=Qt.AlignmentFlag.AlignHCenter)


        self.title_selector = QLabel("Choose preset:")
        self.title_selector.setAlignment(Qt.AlignmentFlag.AlignLeading)
        layout.addWidget(self.title_selector)

        self.level_selector = QComboBox()
        self.level_selector.addItems(["1 - digits only", "2 - letters + digits", "3 - all printable"])
        layout.addWidget(self.level_selector, alignment=Qt.AlignmentFlag.AlignLeading)

        self.button = QPushButton("Generate")
        self.button.clicked.connect(self.pswd_generation)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignHCenter)



        self.pswd_field = QTextEdit("")
        self.pswd_field.setReadOnly(False)
        self.pswd_field.setFixedHeight(100)
        layout.addWidget(self.pswd_field)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle('GP (2.0)')
        self.setFixedSize(500, 260)

    def clear_input(self):
        self.input.clear()
        if hasattr(self, 'pswd_leng'):
            self.pswd_field.clear()





    def pswd_generation(self):
        text = self.input.text()
        try:
            number = int(float(text))
            if number <= 0:
                self.pswd_field.setText("Error! Enter a positive value!")
                return

            level_index = self.level_selector.currentIndex() + 1

            if level_index == 1:
                result = ''.join(str(random.choice(range(10))) for _ in range(number))
            elif level_index == 2:
                chars = string.ascii_letters + string.digits
                result = ''.join(secrets.choice(chars) for _ in range(number))
            elif level_index == 3:
                result = ''.join(secrets.choice(string.printable.strip()) for _ in range(number))
            else:
                result = "Error!"

            self.pswd_field.setText(f"Your Password:\n{result}")
        except ValueError:
            self.pswd_field.setText("Error!!!.")

    def save_txt(self):
        text = self.pswd_field.toPlainText()
        if not text.strip():
            return

        try:
            with open("pswd.txt", "w", encoding="utf-8") as file:
                file.write(text)
            print("saved to pswd.txt")
        except Exception as e:
            print("Error:", e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

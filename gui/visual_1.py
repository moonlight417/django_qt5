import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Django and PyQt5 Interaction')
        layout = QVBoxLayout()

        self.label = QLabel('Items will be displayed here')
        layout.addWidget(self.label)

        self.button = QPushButton('Fetch Items')
        self.button.clicked.connect(self.fetch_items)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def fetch_items(self):
        response = requests.get('http://127.0.0.1:8000/items/')
        if response.status_code == 200:
            items = response.json()
            self.label.setText('\n'.join([item['name'] for item in items]))
        else:
            self.label.setText('Failed to fetch items')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
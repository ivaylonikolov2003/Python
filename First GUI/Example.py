import sys
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtWidgets import (QMainWindow, QLabel, QApplication, QWidget,
                             QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("images.jfif"))
        self.initUI()

        label = QLabel("CSKA SOFIA", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: red;"
                            "background-color: white;"
                            "font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)

        label = QLabel(self)
        label.setGeometry(0, 0, 100, 100)
        pixmap = QPixmap("CSKA_Sofia_Logo_2020.png")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1 The most successful club in Bulgaria ", self)
        label1.setFont(QFont("Arial", 10))
        label2 = QLabel("#2 Killer of European champions", self)
        label2.setFont(QFont("Arial", 10))

        label1.setStyleSheet("background-color: red")
        label2.setStyleSheet("background-color: white")

        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0 , 1)

        central_widget.setLayout(grid)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
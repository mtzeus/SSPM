import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QSlider, QPushButton
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QTimer
import psutil

class OverlayWindow(QWidget):
    def __init__(self, transparency):
        super().__init__()

        self.setWindowTitle("Monitor de Desempenho")
        self.setGeometry(0, 0, 300, 100)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(transparency / 100)

        self.cpu_label = QLabel(self)
        self.cpu_label.move(10, 10)
        self.cpu_label.setFont(QFont("Arial", 12))
        self.cpu_label.setStyleSheet("color: white")

        self.ram_label = QLabel(self)
        self.ram_label.move(10, 40)
        self.ram_label.setFont(QFont("Arial", 12))
        self.ram_label.setStyleSheet("color: white")

        self.disk_label = QLabel(self)
        self.disk_label.move(10, 70)
        self.disk_label.setFont(QFont("Arial", 12))
        self.disk_label.setStyleSheet("color: white")

        self.update_labels()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_labels)
        self.timer.start(1000)  # Atualiza os indicadores a cada segundo

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), QColor(30, 30, 30, 180))

    def update_labels(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        ram_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent

        self.cpu_label.setText(f"CPU: {cpu_percent}%")
        self.ram_label.setText(f"RAM: {ram_percent}%")
        self.disk_label.setText(f"Disco: {disk_percent}%")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    transparency = 80  # Defina a transparência desejada
    overlay = OverlayWindow(transparency)
    overlay.show()

    sys.exit(app.exec())

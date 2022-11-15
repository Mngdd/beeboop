from PyQt5 import uic
import sys
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.paint_mode = True
        self.b.clicked.connect(self.repaint)

    def paintEvent(self, event):
        if self.paint_mode:
            self.paint_mode = False
            qp = QPainter()
            qp.begin(self)
            self.draw_smth(qp)
            self.paint_mode = True
            qp.end()

    def draw_smth(self, qp):  # 1 triang sp 2 circ lmb 3 sq rmb
        a, b, c = randint(0, 255), randint(0, 255), randint(0, 255)
        pen = QBrush(QColor('yellow'), Qt.SolidPattern)
        qp.setBrush(pen)
        mn, mxy, mxx = 10, self.size().height(), self.size().width()
        size1, x, y = randint(mn, 150), randint(mn, mxx), randint(mn, mxy)
        qp.drawEllipse(x, y, size1, size1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

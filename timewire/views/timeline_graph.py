from typing import List

from PySide2.QtCore import QRectF, Qt
from PySide2.QtGui import QPainter, QColor, QPen, QBrush
from PySide2.QtQuick import QQuickPaintedItem
import math
from timewire.views.graph_colors import Color


class TimelineGraph(QQuickPaintedItem):
    def __init__(self, parent=None, draw_border: bool = False):
        QQuickPaintedItem.__init__(self, parent)
        self.title = None
        self.labels: List[str] = ["Default"]
        self.x_padding = 16
        self.y_padding = 16
        self.font_size = 12
        self.draw_border = draw_border
        self.max_width = 10
        self.bar_gap = 2
        self.axis_width = 6

    def set_labels(self, labels: List[str]):
        self.labels = labels

    def paint(self, p: QPainter):
        pen = QPen(QColor(*Color.WHITE))
        p.setPen(pen)

        real_width = int(self.width() - 2 * self.x_padding)
        real_height = int(self.height() - 2 * self.y_padding)

        p.drawRect(self.x_padding, self.y_padding, real_width, real_height)

        bar_amount = 12 * 6  # One bar every 10 minutes

        bar_width = min(math.floor(real_width / bar_amount - self.bar_gap), self.max_width)

        p.setBrush(QColor(*Color.GREEN))
        for i in range(bar_amount):
            p.drawRect(self.x_padding + self.axis_width + self.bar_gap + i * (bar_width + self.bar_gap), self.y_padding, bar_width, real_height)

        # Draw lines
        p.setBrush(QColor(*Color.DARK))
        p.setPen(Qt.NoPen)
        p.drawRect(self.x_padding, self.y_padding + real_height - self.axis_width, real_width, self.axis_width)
        p.drawRect(self.x_padding, self.y_padding, self.axis_width, real_height)

from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsItem


class ConnectibleEllipse(QGraphicsEllipseItem):
    def __init__(self):
        super(ConnectibleEllipse, self).__init__()
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        print("Paint")
        rect = QRectF(0,0, 20,20 )
        brush = QBrush(Qt.blue)

        painter.drawEllipse(rect)
        pass

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        super().mousePressEvent(QGraphicsSceneMouseEvent)

    def dragMoveEvent(self, QGraphicsSceneDragDropEvent):
        print("MOVEE")
        super().dragMoveEvent(QGraphicsSceneDragDropEvent)
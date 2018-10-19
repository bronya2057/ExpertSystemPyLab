from PyQt5 import QtGui, QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QItemDelegate, QComboBox, QStyle


# class ColumnButtonDelegate(QItemDelegate):
#         def setEditorData(self, editor, index):
#             editor.blockSignals(True)
#             editor.setCurrentIndex(int(index.model().data(index)))
#             editor.blockSignals(False)
#
#         def __init__(self) -> None:
#             super().__init__()
#
#         def paint(self, painter, option, index):
#             super().paint(painter, option, index)
#
#         def editorEvent(self, event, model, option, index):
#             return super().editorEvent(event, model, option, index)
#
#         def createEditor(self, parent, option, index):
#             combo = QtWidgets.QComboBox(parent)
#             li = []
#             li.append("Zero")
#             li.append("One")
#             li.append("Two")
#             li.append("Three")
#             li.append("Four")
#             li.append("Five")
#             combo.addItems(li)
#             self.connect(combo, QtCore.SIGNAL("currentIndexChanged(int)"),
#                          self, QtCore.SLOT("currentIndexChanged()"))
#             return combo
#
#         @QtCore.pyqtSlot()
#         def currentIndexChanged(self):
#             self.commitData.emit(self.sender())
#
#         def setModelData(self, editor, model, index):
#             model.setData(index, editor.currentIndex())

class ColumnButtonDelegate(QItemDelegate):

    def __init__(self, owner, itemslist):
        QItemDelegate.__init__(self, owner)
        self.itemslist = itemslist

    def paint(self, painter, option, index):
        # Get Item Data
        #  value = str(index.data(Qt.DisplayRole))
        # fill style options with item data
        style = Qt.QApplication.style()
        opt = QtWidgets.QStyleOptionComboBox()
        opt.currentText = "HI"
        opt.rect = option.rect

        # draw item data as ComboBox
        style.drawComplexControl(QStyle.CC_ComboBox, opt, painter)

    def createEditor(self, parent, option, index):
        # create the ProgressBar as our editor.
        editor = QComboBox(parent)
        editor.addItems(self.itemslist)
        editor.setCurrentIndex(0)
        editor.installEventFilter(self)
        return editor

    def setEditorData(self, editor, index):
        value = 1
        editor.setCurrentIndex(value)

    def setModelData(self, editor, model, index):
        value = editor.currentIndex()
        model.setData(index, QtCore.QVariant(value))

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

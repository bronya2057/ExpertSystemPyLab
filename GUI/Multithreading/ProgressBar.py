# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ProgressBar.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

from GUI.Multithreading.HelperThread import HelperThread


class Ui_StereoscopicConfiguration(object):
    def setupUi(self, StereoscopicConfiguration):
        StereoscopicConfiguration.setObjectName("StereoscopicConfiguration")
        StereoscopicConfiguration.resize(881, 472)
        self.gridLayout_4 = QtWidgets.QGridLayout(StereoscopicConfiguration)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget = QtWidgets.QWidget(StereoscopicConfiguration)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 1, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButtonStop = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonStop.setObjectName("radioButtonStop")
        self.gridLayout.addWidget(self.radioButtonStop, 1, 0, 1, 1)
        self.radioButtonReset = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonReset.setObjectName("radioButtonReset")
        self.gridLayout.addWidget(self.radioButtonReset, 2, 0, 1, 1)
        self.radioButtonStart = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonStart.setObjectName("radioButtonStart")
        self.gridLayout.addWidget(self.radioButtonStart, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 1, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.widget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 3, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(StereoscopicConfiguration)
        QtCore.QMetaObject.connectSlotsByName(StereoscopicConfiguration)
        ########CONNECT SECT#########
        self.radioButtonStart.clicked.connect(self.on_start_clicked)
        self.radioButtonStop.clicked.connect(self.on_stop_clicked)
        self.radioButtonReset.clicked.connect(self.on_reset_clicked)
        self.progress_value = 0
        #############################

    def progressbar_counter(self, start_value=0):
        self.run_thread = HelperThread(parent=None, counter_start=start_value)
        self.run_thread.start() # instance variable runs the run() method
        self.run_thread.counter_value.connect(self.set_progressbar)  # connect to the emmiter from HelperThread

    def set_progressbar(self, counter):  # after each update emmited signal calls this slot
        if not self.stop_progress:
            self.progressBar.setValue(counter)

    def on_start_clicked(self):
        print("start")
        self.stop_progress = False
        self.progress_value = self.progressBar.value()
        self.progressbar_counter(self.progress_value)

    def on_stop_clicked(self):
        print("stop")
        self.stop_progress = True
        try: self.run_thread.stop()
        except:pass

    def on_reset_clicked(self):
        print("reset")
        self.on_stop_clicked()
        self.progress_value = 0
        self.stop_progress = False
        self.progressBar.reset()

    def retranslateUi(self, StereoscopicConfiguration):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("StereoscopicConfiguration", "GroupBox"))
        self.radioButtonStop.setText(_translate("StereoscopicConfiguration", "Stop"))
        self.radioButtonReset.setText(_translate("StereoscopicConfiguration", "Reset"))
        self.radioButtonStart.setText(_translate("StereoscopicConfiguration", "Start"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    StereoscopicConfiguration = QtWidgets.QWidget()
    ui = Ui_StereoscopicConfiguration()
    ui.setupUi(StereoscopicConfiguration)
    StereoscopicConfiguration.show()
    sys.exit(app.exec_())

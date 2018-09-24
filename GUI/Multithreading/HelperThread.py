from time import sleep

from PyQt5 import QtCore


class HelperThread(QtCore.QThread):
    counter_value = QtCore.pyqtSignal(int)  # define new signal

    def __init__(self, parent=None, counter_start=0):
        super(HelperThread, self).__init__(parent)
        self.counter = counter_start
        self.is_running = True

    def run(self):
        while self.counter < 100 and self.is_running == True:
            sleep(0.1)
            self.counter += 1
            print(self.counter)
            self.counter_value.emit(self.counter)  # emit new Signal and catch it in progress bar

    def stop(self):
        self.is_running = False
        print("stopping thread...")
        self.terminate()

# import sys
# from PyQt5 import QtCore, AtGui, QtWidgets
# from des *

# class Gui(QtWidgets,QMainWindow) :
#     def __init__(Self, parent=None):
#         super().__init__(parent)
#         self.ui = Ui_MainWindow()
#         self.ui.pushButton.clicked.connect(self.set_buf)

#         self.clipboard = QtWidgets.QApplication.clipboard()
#         self.clipboard.setPixmap(QtGui.QPixmap('1.jpeg'))


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()фss

#         # Устанавливаем размеры окна
#         self.setGeometry(200, 200, 640, 480)

#     def keyPressEvent(self, event):
#         # Проверяем, нажата ли клавиша A
#         if event.key() == Qt.Key_A:
#             print("A key pressed")


# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec_())


# def event_filter(obj, event):
#     if event.type() == QEvent.KeyPress:
#         # Check if the "S" key was pressed
#         if event.key() == Qt.Key_S:
#             # Capture a screenshot of the entire desktop
#             screenshot = QGuiApplication.primaryScreen().grabWindow(0)

#             # Save the screenshot to a file
#             screenshot.save("screenshot.png")

#             # Set the screenshot as the label's pixmap
#             label.setPixmap(screenshot)
#     return False


# # Install the event filter on the label
# label.installEventFilter(event_filter)

# app.exec_()


# class Gui(QtWidgets,QMainWindow) :
#     def __init__(Self, parent=None):
#         super().__init__(parent)
#         self.ui = Ui_MainWindow()
#         self.ui.pushButton.clicked.connect(self.set_buf)

#         self.clipboard = QtWidgets.QApplication.clipboard()
#         self.clipboard.setPixmap(QtGui.QPixmap('1.jpeg'))

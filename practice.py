import keyboard
# import pyperclip
import pyautogui
import sys
# import time
from PyQt5.QtGui import QPixmap, QGuiApplication
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtTest import QTest
# from PyQt5.QtCore import Qt
# from PIL import Image, ImageQt


app = QGuiApplication(sys.argv)


# def on_a_key_press(event):
#     print('as')
#     # скрин с помощью qt
#     screenshot = QGuiApplication.primaryScreen().grabWindow(0)
#     screenshot.save("screenshot.png")

#     # преобразовать
#     # image = Image.open("im2.png")
#     # pixmap = ImageQt.toqpixmap(image)

#     # сделать скрин
#     # im2 = pyautogui.screenshot('im2.jpeg')

#     # сохранить в бо
#     clipboard = QGuiApplication.clipboard()
#     clipboard.setPixmap(screenshot)

#     # pyautogui.hotkey('ctrl', 'v')


# keyboard.on_press_key("a", on_a_key_press)

# keyboard.wait()
screenshot = QGuiApplication.primaryScreen().grabWindow(0)
screenshot.save("screenshot.png")
clipboard = QGuiApplication.clipboard()
clipboard.setPixmap(screenshot)

sys.exit(app.exec_())


# len = length
# continue
# delef
# append = push
# insert = push в определнный индекс без замены
# count for arr = сколько элемента в массиве
# sort
# reverse
# pop удалить или схавать
# remove(2) удалить совпадающие
# exstend это constant
# copy array

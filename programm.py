import pyautogui
import sys
import time
from PyQt5.QtGui import QPixmap, QGuiApplication

app = QGuiApplication(sys.argv)

screenshot = QGuiApplication.primaryScreen().grabWindow(0).copy(90, 90, 860, 900)
screenshot.save("screenshot.png")

clipboard = QGuiApplication.clipboard()
clipboard.setPixmap(screenshot)
time.sleep(0.5)

pyautogui.hotkey('ctrl', 'v')
sys.exit()


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

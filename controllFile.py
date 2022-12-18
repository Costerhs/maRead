import keyboard
import subprocess

process = None
print('hi')


def start_process():
    global process
    process = subprocess.Popen(
        ["python", "D:\pythonCodes\pythonPractice\programm.py"])


keyboard.add_hotkey("o", start_process)

keyboard.wait()

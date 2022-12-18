import keyboard
import subprocess

process = None
print('hi')


def start_process():
    global process
    process = subprocess.Popen(
        ["python", "D:\pythonCodes\pythonPractice\practice.py"])


def stop_process():
    global process
    process.kill()


keyboard.add_hotkey("o", start_process)
keyboard.add_hotkey("c", stop_process)

keyboard.wait()

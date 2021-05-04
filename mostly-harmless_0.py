# 0
import os, sys, subprocess, time, pyautogui
number = __file__.split('_', 1)[1]
number = int(number[:len(number)-3]) + 1
filePath = f'{os.getcwd()}/mostly-harmless_{number}.py'
file = open(filePath, 'w').close()
subprocess.Popen(['notepad.exe', filePath])
time.sleep(1)
with open(__file__, 'r') as currentFile:
    lines = currentFile.readlines()[1:]
    pyautogui.typewrite(f'# {number}\n', interval=0.05)
    for line in lines:
        pyautogui.typewrite(line, interval=0.05)
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('alt', 'f4')
subprocess.Popen(['start', sys.executable, filePath], shell=True)
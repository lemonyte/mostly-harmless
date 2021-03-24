# 0
import os, sys, subprocess, time, pyautogui
number = __file__.split("_", 1)[1]
number = int(number[:len(number)-3]) + 1
filePath = str(os.getcwd() + "\\mostly-harmless_%s.py" % number)
file = open(filePath, "w")
file.close()
subprocess.Popen(["notepad.exe", filePath])
time.sleep(1)
with open(__file__, "r") as currentFile:
    lines = currentFile.readlines()[1:]
    pyautogui.typewrite("# %s\n" % number, interval=0.05)
    for line in lines:
        pyautogui.typewrite(line, interval=0.05)
    pyautogui.hotkey("ctrl", "s")
    pyautogui.hotkey("alt", "f4")
subprocess.Popen(["start", sys.executable, filePath], shell=True)
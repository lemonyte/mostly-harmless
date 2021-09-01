# 0
import os, sys, subprocess, time, pyautogui
number = int(__file__.split('_', 1)[1][:-3]) + 1
new_file = f"{os.getcwd()}/{__file__.split('_', 1)[0]}_{number}.py"
open(new_file, 'w').close()
subprocess.Popen(['notepad.exe', new_file])
time.sleep(1)
with open(__file__, 'r') as current_file:
    lines = current_file.readlines()[1:]
    pyautogui.typewrite(f'# {number}\n', interval=0.05)
    for line in lines:
        pyautogui.typewrite(line, interval=0.05)
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('alt', 'f4')
subprocess.Popen(['start', sys.executable, new_file], shell=True)

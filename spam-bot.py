import pyautogui,time
time.sleep(3)
msg ="This is a spam message."
for i in range(10000):
    pyautogui.typewrite(msg)
    pyautogui.press("enter")
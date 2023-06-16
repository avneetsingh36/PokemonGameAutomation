# This script will take control of your computer (to some extent) to help you take steps to level up your Pokemon in DayCare --> Check out README.md for more details!

import pyautogui
import keyboard
from time import sleep

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

sleep(3)

# Uncomment if you wanna test that it clicks a certain portion of your screen
#pyautogui.click(160,60)
#sleep(1)

for i in range(10):
    c1 = 50
    c2 = 50
    while c1 > 0:
        pyautogui.press('up')
        c1-=1
    while c2 > 0:
        pyautogui.press('down')
        c2-=1

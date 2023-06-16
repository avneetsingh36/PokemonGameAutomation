# This script will take control of your computer (to some extent) to help you take steps to level up your Pokemon in DayCare --> Check out README.md for more details!

# Import necessary libraries
import pyautogui
import keyboard
from time import sleep

x = 10
y = 10

# Log and Print screen dimentions so that you know exactly which monitor is being used (this can be removed)
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
sleep(2)

# Uncomment if you want test that it clicks a certain portion of your screen; make sure to set the x and y position above
pyautogui.click(x,y)
sleep(2)

for i in range(10):
    c1 = 50
    c2 = 50
    while c1 > 0:
        pyautogui.press('up')
        c1-=1
    while c2 > 0:
        pyautogui.press('down')
        c2-=1
        
print('Done')

# This file helps you find which coordinates you want on your screen based on mouse position; runs until you kill the program and prints out in your terminal.

import pyautogui

for _ in range(10):
    currentMouseX, currentMouseY = pyautogui.position()
    print(f'x: {currentMouseX} | y: {currentMouseY}')

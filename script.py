# This script will take control of your computer (to some extent) 
# to help you take steps to level up your Pokemon in DayCare 
# --> Check out README.md for more details!

# Import necessary libraries
import pyautogui
from time import sleep

def get_screen_size():
    """Log and print screen dimensions"""
    screen_width, screen_height = pyautogui.size()
    print(screen_width, screen_height)
    sleep(2)
    return screen_width, screen_height

def click_position(x, y):
    """Click a specific position on screen"""
    pyautogui.click(x, y)
    sleep(2)

def press_keys():
    """Simulate key presses"""
    for i in range(10):
        c1 = 50
        c2 = 50
        while c1 > 0:
            pyautogui.press('up')
            c1 -= 1
        while c2 > 0:
            pyautogui.press('down')
            c2 -= 1

def main():
    get_screen_size()

    # Uncomment the following line and set x and y to test if it clicks a certain portion of your screen.
    # This allows you to have the necessary tab clicked as a part of the automation process.
    # click_position(x, y)
    
    press_keys()

    print('Done')

if __name__ == "__main__":
    main()


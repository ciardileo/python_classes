from pyautogui import *

while True:
    points = locateCenterOnScreen('images/rock_gold.png')
    click(points)
    print(points)
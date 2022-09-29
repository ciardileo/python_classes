import pyautogui as pt
import time

# escrever na caixa de texto

time.sleep(6)

while True:
    pt.typewrite('teste')

    time.sleep(0.6)
    # aperta uma tecla (menos as setas)

    pt.press('enter')
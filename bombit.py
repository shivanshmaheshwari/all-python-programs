import pyautogui as pg
import time
time.sleep(5)
for i in range(1000):
    pg.typewrite('hello')
    pg.press('enter')

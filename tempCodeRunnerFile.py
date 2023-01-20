import pyautogui as pg
import time
time.sleep(5)
for i in range(1000):
    pg.write('hello ', i)
    pg.press('enter')

import pyautogui as pg
import time

print("program will run in 5 sec")
time.sleep(5)

for i in range(100):
    pg.write("This is Jarvis. A program from NIX's laptop, __I can message on whatsapp__")
    time.sleep(0.5)
    pg.press("Enter")
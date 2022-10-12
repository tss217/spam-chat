

import pyautogui as spam
import time

limite = input("limite:")
msg = input("msg:")

i = 0

time.sleep(5)

while i <int(limite):
    spam.typewrite(msg)
    spam.press("Enter")
    i+=1
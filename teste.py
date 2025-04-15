import time
import pyautogui

# time.sleep(1)
# # email = ["carecamateus22@gmail.com.br , ","tadeu@nutripar.com.br , ","vendas@nutripar.com.br , ","ederson@nutripar.com.br"]

# email = ["mateussilverio2707@hotmail.com , ","carecamateus22@gmail.com.br , ","ederson@nutripar.com.br"]
# for destinatario in email:
#     pyautogui.write(destinatario) # escrevo o email
#     print(destinatario)
#     time.sleep(1)
time.sleep(3)
pyautogui.hotkey("win", "d")
time.sleep(1)

pyautogui.click(x=32, y=57)
pyautogui.press("del")
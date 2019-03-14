from PIL import Image
import pytesseract
import os
import pyautogui
import time

#time.sleep(5)

#pic = pyautogui.screenshot()
#pic.save('aa.png')
print(pytesseract.image_to_string(Image.open('aa.png'))) # Extraindo o texto da imagem

pyautogui.moveTo('dieite.png')

os.system('pause')

import pyautogui
from datetime import datetime
import time

agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

pyautogui.press("winleft")  
time.sleep(1)  
pyautogui.write("chrome")  
time.sleep(1)  
pyautogui.press("enter")  
time.sleep(2) 
pyautogui.moveTo(244, 60, duration=0.5) 
time.sleep(1)
pyautogui.click()
pyautogui.write("dolar investing", interval=0.10)
time.sleep(1)
pyautogui.press("enter")
pyautogui.moveTo(515, 307, duration=0.7)
time.sleep(1)
pyautogui.click()
time.sleep(5)
pyautogui.screenshot("screenshots/dolar.png")
# pyautogui.alert(text="Screenshot taken", title="Automation Complete", button="OK")
pyautogui.moveTo(315, 28, duration=0.7)
pyautogui.click()
pyautogui.moveTo(301, 70, duration=0.7)
pyautogui.click()
pyautogui.write("https://web.whatsapp.com/", interval=0.10)
time.sleep(1)
pyautogui.press("enter")
time.sleep(8)
pyautogui.moveTo(465, 520, duration=0.7) #grupo
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(750, 987, duration=0.7)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(841, 677, duration=0.7)
pyautogui.click()




import pyautogui as pa
import time
import pyperclip
# x1 = pyautogui.locateCenterOnScreen('Data/icon1.PNG')
# pyautogui.doubleClick(x1)

chrome = pa.locateCenterOnScreen('Data/chrome.PNG')
pa.doubleClick(chrome)

time.sleep(1)
pyperclip.copy('www.kpu.ac.kr')
pa.hotkey('ctrl',"v")
pa.press('enter')
time.sleep(1)
pa.hotkey('f11')
time.sleep(1)
pa.click(949,484)
time.sleep(2)
pa.click(1001,14)
time.sleep(2)
pa.click(716,299)

pa.typewrite('2016182007')
pa.press('tab')
pa.typewrite('dn97389738!')
pa.press('enter')
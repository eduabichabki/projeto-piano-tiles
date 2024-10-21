import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

pyautogui.click(1538,505, duration=1)

def clicar(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed("1") == False:
    if pyautogui.pixelMatchesColor(1420,443, (0,0,0)):
        clicar(1420,443)
    if pyautogui.pixelMatchesColor(1499,441, (0,0,0)):
        clicar(1499,441)
    if pyautogui.pixelMatchesColor(1579,441, (0,0,0)):
        clicar(1579,441)
    if pyautogui.pixelMatchesColor(1650,434, (0,0,0)):
        clicar(1650,434)
from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()
keyboard.press(Key.cmd) #Alt
sleep(0.3)
keyboard.press(Key.tab) #Tab
sleep(0.3)
keyboard.release(Key.tab) #~Tab
sleep(0.3)
keyboard.release(Key.cmd) #~Alt

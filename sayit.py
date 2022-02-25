import pyautogui, time

DELAY = 5

f = open('pins.txt').readlines()


for _ in range(DELAY):
  DELAY -= 1

  print(f'Timer ending in {DELAY}', end='\r')
  time.sleep(1)

for i in f:
  pyautogui.typewrite(i)
  pyautogui.press('enter')


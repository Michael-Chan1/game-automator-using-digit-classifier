import pyautogui
import cv2

# TFT TIME
# 754 - 806 x
# 0 - 30 y

im = pyautogui.screenshot()

im = im.crop((754, 5, 806, 35))

im.save('ss/color_stage.jpg')

cv2Image = cv2.imread('ss/color_stage.jpg')

grey = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('ss/stage.jpg', grey)

import pyautogui
import cv2
import numpy as np
import time
import keyboard
from PIL import Image
from keras.models import load_model

def getImages():
    # Gets the images of the numbers and grey scales the image
    im = pyautogui.screenshot()
    digit1 = im.crop((750, 5, 778, 33))
    digit2 = im.crop((783, 5, 811, 33))

    digit1.save('ss/stage.jpg')
    digit2.save('ss/level.jpg')

    cv2D1 = cv2.imread('ss/stage.jpg')
    cv2D2 = cv2.imread('ss/level.jpg')

    grey1 = cv2.cvtColor(cv2D1, cv2.COLOR_BGR2GRAY)
    grey2 = cv2.cvtColor(cv2D2, cv2.COLOR_BGR2GRAY)

    (thresh, blackAndWhiteImage) = cv2.threshold(
        grey1, 127, 255, cv2.THRESH_BINARY)
    (thresh2, blackAndWhiteImage2) = cv2.threshold(
        grey2, 127, 255, cv2.THRESH_BINARY)

    blackAndWhiteImage = np.expand_dims(blackAndWhiteImage, 2)
    blackAndWhiteImage2 = np.expand_dims(blackAndWhiteImage2, 2)

    cv2.imwrite('ss/stage.jpg', blackAndWhiteImage)
    cv2.imwrite('ss/level.jpg', blackAndWhiteImage2)



def enterGame():
    # Accepts queue
    time.sleep(5)
    pyautogui.click(1000, 740)
    
    
def ff():
    # Surrenders
    time.sleep(60)
    keyboard.press_and_release('enter')
    keyboard.press_and_release('/')
    keyboard.press_and_release('f')
    keyboard.press_and_release('f')
    keyboard.press_and_release('enter')
    time.sleep(1)
    pyautogui.moveTo(900, 480, 2)
    pyautogui.mouseDown(); pyautogui.mouseUp()
    
def restart():
    # Enter the queue again
    time.sleep(10)
    pyautogui.click(900, 850)
    time.sleep(10)
    pyautogui.click(900, 850)
    
    
def is_three_one():
    # Checks in the stage is three_one
    getImages()
    model = load_model("digit.h5")
    cv2D1 = cv2.imread('ss/stage.jpg')
    cv2D2 = cv2.imread('ss/level.jpg')
    M = np.float32([[1, 0, -7], [0, 1, 0]]) 
    (rows, cols) = cv2D1.shape[:2] 
    res = cv2.warpAffine(cv2D1, M, (cols, rows)) 

    cv2.imwrite('ss/stage.jpg', res) 

    M = np.float32([[1, 0, 8], [0, 1, 0]]) 
    (rows, cols) = cv2D2.shape[:2] 
    res = cv2.warpAffine(cv2D2, M, (cols, rows)) 

    cv2.imwrite('ss/level.jpg', res)
    cv2D1 = cv2.imread('ss/stage.jpg')
    cv2D2 = cv2.imread('ss/level.jpg')
    gray1 = cv2.cvtColor(cv2D1, cv2.COLOR_BGR2GRAY)
    gray1 = gray1.flatten()
    pred1 = model.predict(np.array([gray1]))[0]
    gray2 = cv2.cvtColor(cv2D2, cv2.COLOR_BGR2GRAY)
    gray2 = gray2.flatten()
    pred2 = model.predict(np.array([gray2]))[0]
    return (pred1.argmax() == 3 and pred2.argmax() == 1)
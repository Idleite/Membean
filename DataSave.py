# Python program to take 
# screenshots 


import numpy as np 
import cv2 
import pyautogui 
import os

# take screenshot using pyautogui 
image = pyautogui.screenshot() 
print(image.show())
# since the pyautogui takes as a 
# PIL(pillow) and in RGB we need to 
# convert it to numpy array and BGR 
# so we can write it to the disk 
image = cv2.cvtColor(np.array(image), 
					cv2.COLOR_RGB2BGR)
print(image)
PathRelative = "image1.png"
# writing it to the disk using opencv
x = cv2.imwrite(PathRelative, image)
print(x)

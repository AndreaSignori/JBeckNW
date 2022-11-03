import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture()
# initialize the Vision class
vision_A = Vision('A.png')
vision_D = Vision('D.png')
vision_M = Vision('M.png')
vision_S = Vision('S.png')
vision_Space = Vision('Space.png')
vision_W = Vision('W.png')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    screenshot = screenshot[700:940 , 530:640]
    # display the processed image
    points = vision_A.find(screenshot, 0.7, 'rectangles','a')
    points = vision_D.find(screenshot, 0.7, 'rectangles','d')
    points = vision_M.find(screenshot, 0.7, 'rectangles','Mouse')
    points = vision_S.find(screenshot, 0.7, 'rectangles','s')
    points = vision_Space.find(screenshot, 0.7, 'rectangles',' ')
    points = vision_W.find(screenshot, 0.7, 'rectangles','w')
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')

    # debug the loop rate
    #print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
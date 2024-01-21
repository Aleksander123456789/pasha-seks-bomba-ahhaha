from PIL import Image
import cv2
import numpy as np
import os as os
import math
from matplotlib import pyplot as plt 

arr = []
#generating videofile
def vidGen():
    # Define the dimensions of the image
    width = 50
    height = 50
    #code was stolen :)
    def generateImgSqr(x, y, a):
        # Create a new image with the defined dimensions and black background
        image = Image.new("RGB", (width, height), "black")
        # Access the pixel values and modify them
        pixels = image.load()
        for x1 in range(width):
            for y1 in range(height):
                # Assign a unique pixel value based on the x and y coordinates
                if((x1>x-a and x1<x+a) and (y1>y-a and y1<y+a)):
                    pixels[x1, y1] = (255, 255, 255)
        # Save the image
        s = "pixel_values.png"
        image.save(s)
        #read it w/ OpenCV
        arr.append(cv2.imread(s))
        #remove image file
        os.remove(s)
    def generateMoveingSqr(x0, y0, x1, y1, t, a):
        x, y = x0, y0
        print("stat: ", x, y, x1, y1, x0, y0)            
        while(((x <= x1 and x1 >= x0) or (x >= x1 and x1 <= x0)) and ((y <= y1 and y1 >= y0) or (y >= y1 and y1 <= y0))):
            x += int((x1 - x0) / t)
            y += int((y1 - y0) / t)
            generateImgSqr(x, y, a)
    generateMoveingSqr(15, 15, 30, 30, 10, 5)
    generateMoveingSqr(30, 30, 25, 20, 10, 5)
    #making all frames in arr[] into a videofile
    video = cv2.VideoWriter(
        filename="output.mp4", fourcc=cv2.VideoWriter_fourcc(*"mp4v"), fps=5.0, frameSize=(width, height)
    ) 
    for i in range(len(arr)):
        video.write(arr[i])
    video.release()
    #:)
    print("Video generated")
def markCorners():
    cap = cv2.VideoCapture('output.mp4')
    frameRate = cap.get(5) #frame rate
    #processing video
    while(cap.isOpened()):
        frameId = cap.get(1) #current frame number
        ret, frame = cap.read()
        if (ret != True):
            break
        if (frameId % math.floor((frameRate*t)) == 0):
            print("----- PROCESSING NEW FRAME -----")
            print("FrameIndex:", frameId)
            #turning img to binary(only black and white)
            re, binary_image = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)
            white = np.argwhere(np.array(np.sum(binary_image, axis=-1) == 765, dtype=np.int32))
            print("Upper-Left:", np.min(white[white[:, 0] == np.min(white[:, 0])], 0)[0], np.min(white[white[:, 0] == np.min(white[:, 0])], 0)[1])
            print("Down-Right:", np.max(white[white[:, 0] == np.max(white[:, 0])], 0)[0], np.max(white[white[:, 0] == np.max(white[:, 0])], 0)[1])
            print("Delta:", (np.max(white[white[:, 0] == np.max(white[:, 0])], 0)[0] - np.min(white[white[:, 0] == np.min(white[:, 0])], 0)[0]), (np.max(white[white[:, 0] == np.max(white[:, 0])], 0)[1] - np.min(white[white[:, 0] == np.min(white[:, 0])], 0)[1]))
            print("Middle:", np.min(white[white[:, 0] == np.min(white[:, 0])], 0)[0] + (np.max(white[white[:, 0] == np.max(white[:, 0])], 0)[0] - np.min(white[white[:, 0] == np.min(white[:, 0])], 0)[0])//2, np.min(white[white[:, 0] == np.min(white[:, 0])], 0)[1] + (np.max(white[white[:, 0] == np.max(white[:, 0])], 0)[1] - np.min(white[white[:, 0] == np.min(white[:, 0])], 0)[1])//2)
            #color the most top-left white pixel greer G R E E R
            binary_image[np.min(white[white[:, 0] == np.min(white[:, 0])], 0)[0], np.min(white[white[:, 0] == np.min(white[:, 0])], 0)[1]] = [0, 255, 0]
            #color the most down-right white pixel red
            binary_image[np.max(white[white[:, 0] == np.max(white[:, 0])], 0)[0], np.max(white[white[:, 0] == np.max(white[:, 0])], 0)[1]] = [255, 0, 0]
            
            binary_image[np.min(white[white[:, 0] == np.min(white[:, 0])], 0)[0] + (np.max(white[white[:, 0] == np.max(white[:, 0])], 0)[0] - np.min(white[white[:, 0] == np.min(white[:, 0])], 0)[0])//2, np.min(white[white[:, 0] == np.min(white[:, 0])], 0)[1] + (np.max(white[white[:, 0] == np.max(white[:, 0])], 0)[1] - np.min(white[white[:, 0] == np.min(white[:, 0])], 0)[1])//2] = [0, 0, 255]
            #showing da img
            plt.imshow(binary_image), plt.show()
    cap.release()
#how much time in seconds between processing frames
t = float(input("dt: "))
#generating video
vidGen()
#marking cornr
markCorners()
print("done")
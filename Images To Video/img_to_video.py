import cv2
import numpy as np
import glob


def imgToVideo(in_Path, out_Path, fps=20):
    '''
    in_Path: path to folder in glob.glob style, end with /*.png(.jpeg, .jpg)
    out_Path: path to the output, ends with .avi
    fps: frames per second, default is 20
    '''
    
    img_array = []
    for filename in glob.glob(in_Path):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)


    out = cv2.VideoWriter(out_Path,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
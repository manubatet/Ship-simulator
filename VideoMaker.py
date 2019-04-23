 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:23:49 2019

@author: manuelbatet
"""

import os
import argparse
import cv2
import glob
import sys

#save actual path
act_path = os.getcwd()


def VideoMaker(input_folder, output_folder):
    sys.path.append(input_folder)
    from parameters import FRAME_INTERVAL  
    frames =sorted( glob.glob(input_folder + '/*.png'), key=lambda x: int(x[(x.rfind('/')+1):x.find('.png')]) )
#initialize the img_array
    img_array=[]
    for filename in frames:    
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    #if there were some frames continue    
    if len(frames)>0: 
        os.chdir(output_folder)
        out = cv2.VideoWriter('Video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 20/FRAME_INTERVAL, size)
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()
        print('videos have been saved in ' + output_folder)
                                            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Specify desktop path')
    parser.add_argument('-i', '--input_folder', help='Path of the forder where the frames are', type=str)
    parser.add_argument('-o', '--output_folder', help='Path where you want to put the video', type=str)
    args = parser.parse_args()

    VideoMaker(args.input_folder, args.output_folder)

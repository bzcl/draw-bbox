# -*- coding: utf-8 -*-

import cv2
import os


def main():
    gtpath='./gt'
    impath='./img'
    simpath='./simg'
    gtfiles=os.listdir(gtpath)
    imfiles=os.listdir(impath)

    for imfile in imfiles:
    	imfilename=os.path.join(impath,imfile)
    	img = cv2.imread(imfilename)
    	with open(os.path.join(gtpath, imfile[:-4] + ".txt"), 'r', encoding='utf-8') as f:
    		for line in f.readlines():
    			line = [int(i) for i in line.strip().split(',')]
    			new_img = cv2.rectangle(img, tuple(line[0:2]), tuple(line[4:6]), (0, 255, 0))
    			simfilename=os.path.join(simpath,imfile)
    			cv2.imwrite(simfilename, new_img)



if __name__ == "__main__":
    main()

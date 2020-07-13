import numpy as np
import os
import glob
import random
import cv2 as cv
import natsort
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import shutil

def rename():
    bground_path = './1일차/' # <-폴더 이름
    bground_list = os.listdir(bground_path)

    for i in bground_list:
        
        real_path = bground_path + i
        gray_img = Image.open(real_path)
        w, h = gray_img.size
        
        k2 = float(190 / w) # 이미지의 크기에서 190으로 resize하려면 얼마나 필요한지 알기위해

        gray_img =gray_img.resize((int(w * k2) , int(h* k2))) # 이미지 w, h 값에 위에서 구한 비율을 곱해준다.
        w2, h2 = gray_img.size # 그렇게 resize된 이미지의 사이즈를 구함
        x = (112-int(w2/2))
        y = (112-int(h2/2))

        images = np.array(gray_img)
        gray = cv.cvtColor(images, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+ cv.THRESH_OTSU)
        pil_image=Image.fromarray(thresh)
        
        save_path = './save/' + str(i)
        example_img = Image.new("L", (224, 224),255)
        example_img.paste(pil_image, (x, y))
        example_img.save(save_path)
                
if __name__ == '__main__':
    rename()
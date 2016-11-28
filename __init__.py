# encoding:utf-8
import os
from PIL import Image 
import re
import shuiyin
# import pyexiv2
import tempfile
import pexif

#图片压缩批处理  
def compressImage(srcPath):  
    dstPath =srcPath+'/压缩图片'
    shuiyin_path =srcPath+'/水印图片'
    for filename in os.listdir(srcPath):  
        #如果不存在目的目录则创建一个，保持层级结构
        if not os.path.exists(dstPath):
                os.makedirs(dstPath)
        if not os.path.exists(shuiyin_path):
                os.makedirs(shuiyin_path)         
        #拼接完整的文件或文件夹路径
        srcFile=os.path.join(srcPath,filename)
        dstFile=os.path.join(dstPath,filename)
        shuiyin_pathFile =os.path.join(shuiyin_path,filename)
        #如果是文件就处理
        if os.path.isfile(srcFile) and re.match(r'^.*.(jpg|png|jpge)$', srcFile):     
            #打开原图片缩小后保存，可以用if srcFile.endswith(".jpg")或者split，splitext等函数等针对特定文件压缩
            sImg=Image.open(srcFile)  
            w,h=sImg.size 
            try:
                img = pexif.JpegFile.fromFile(srcFile)
                orientation = img.exif.primary.Orientation[0]
                print orientation
           
                if orientation is 6: 
                    h,w=sImg.size 
                    sImg = sImg.transpose(Image.ROTATE_270)
                elif orientation is 8: 
                    h,w=sImg.size 
                    sImg = sImg.transpose(Image.ROTATE_90)
                elif orientation is 3: 
                    h,w=sImg.size 
                    sImg = sImg.transpose(Image.ROTATE_180)
                elif orientation is 2: 
                    sImg = sImg.transpose(Image.FLIP_LEFT_RIGHT)
                elif orientation is 5: 
                    h,w=sImg.size 
                    sImg = sImg.transpose(Image.ROTATE_270).transpose(Image.FLIP_LEFT_RIGHT)
                elif orientation is 7: 
                    sImg = sImg.transpose(Image.ROTATE_90).transpose(Image.FLIP_LEFT_RIGHT)
                elif orientation is 4: 
                    h,w=sImg.size 
                    sImg = sImg.transpose(Image.ROTATE_180).transpose(Image.FLIP_LEFT_RIGHT)
            except: pass
#           
            print w,h
            if  w>3000:
                dImg=sImg.resize(((int)(w/3),(int)(h/3)),Image.ANTIALIAS)  #设置压缩尺寸和选项，注意尺寸要用括号
            elif w>2000:
                dImg=sImg.resize(((int)(w/2),(int)(h/2)),Image.ANTIALIAS)  #设置压缩尺寸和选项，注意尺寸要用括号
            elif w>1000:
                dImg=sImg.resize(((int)(w/1.5),(int)(h/1.5)),Image.ANTIALIAS)
            else:
                dImg=sImg.resize((w,h),Image.ANTIALIAS) 
            dImg.save(dstFile) #也可以用srcFile原路径保存,或者更改后缀保存，save这个函数后面可以加压缩编码选项JPEG之类的  
            
            shuiyin.main(dstFile, shuiyin_pathFile)
            print dstFile+" compressed succeeded"
        #如果是文件夹就递归
        if os.path.isdir(srcFile):
            compressImage(srcFile)

if __name__=='__main__':  
    compressImage("/Users/imac/Desktop/诊所信息整理")
#     compressImage("/Users/imac/Desktop/诊所信息整理")








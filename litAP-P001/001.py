# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
# coding:utf-8

"""


def white_to_transparent(img):
    img=img.convert('RGBA') # 返回一个转换后的图像的副本
    datas=img.getdata()
    newData=[]
    for item in datas:
        if item[0]==255 and item[1]==255:
            newData.append((255,255,255,0))
        else:
            newData.append(item)
    img.putdata(newData)    # 赋给图片新的像素数据
    return img

if __name__=="__main__":

    p1_name="github_logo.png"
    p2_name="red_reminder.png"
    # 打开两张png图片，注意为当前路径
    p1_image=Image.open('github_logo.png')
    p2_image=Image.open('red_reminder.png')
    p2_transparent=white_to_transparent(p2_image)
    p1_image.paste(p2_transparent,(0,0),p2_transparent)

    usr_font=ImageFont.truetype(u"./yahei.TTF",32) # 定义字体为微软雅黑
    draw=ImageDraw.Draw('red_reminder.png') # 在p1_image上绘制文字，图像
    draw.text((152,8),u'12',font=usr_font)
    p1_image.save("final.png","PNG")

"""

import os
import sys

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def creat_picture():
    blank=Image.new("RGB",[1024,768],"white")
    drawObject=ImageDraw.Draw(blank)

    # 画直线
    drawObject.line([100,100,100,600],fill = 10)
    drawObject.line([(100,100),600,100],fill = 128)
    drawObject.line([(600,100),(600,600)],"black")
    drawObject.line((100,600,600,600),fill = "yellow")
    #画一个60度蓝色圆弧
    drawObject.arc((100,100,600,600),0,90,fill = "blue")
    #画一个上半圆弧
    drawObject.arc((100,100,600,600),180,360,fill = "red")
    #画一个右半椭圆，只需改区域大小为长方形
    drawObject.arc((100,100,600,400),90,270,fill = "blue")
    # 画圆和椭圆
    drawObject.ellipse((100,100,600,600),outline = 128)
    drawObject.ellipse((100,250,600,450),fill = "blue")

    #画圆
    drawObject.ellipse((100,100,600,600),outline = 128)
    #画一条弦
    drawObject.chord((100,100,600,600),0,90,outline = "red")
    #画弦并且将弦与弧包围区域涂色
    drawObject.chord((100,100,600,600),90,180,fill = "red")

    #画一个圆
    drawObject.ellipse((100,100,600,600),outline = 128)
    #在上一行画出的园内画180度到210度的扇形区域轮廓
    drawObject.pieslice((100,100,600,600),180,210,outline = 128)
    #画60度到90度的扇形区域
    drawObject.pieslice((100,100,600,600),60,90,fill = "blue")

    drawObject.polygon([(200,200),(600,300),(300,600)],outline = "red")
    drawObject.polygon([(300,300),(500,300),(300,500),(500,500)],fill = "red")

    #画矩形
    drawObject.rectangle((200,200,500,500),outline = "red")
    drawObject.rectangle((250,300,450,400),fill = 128)

    #在空白图像上矩形区域内添加文字
    text = "I love python!"
    drawObject.rectangle((200,200,500,500),outline = "red")
    drawObject.text([300,350],text,"red")

    text = "I love python!"
    drawObject.rectangle((100, 100, 600, 600), fill=128)
    # 字体对象1为simsunb，字大小为36号
    Font1 = ImageFont.truetype("C:\Windows\Fonts\simsunb.ttf", 36)
    # 字体对象2在ttc中第一个（我也不知道具体是什么字形），字大小为36号
    Font2 = ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 36, index=0)
    # 字体对象2在ttc中第二个，字大小为36号
    Font3 = ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 36, index=1)
    # 字体对象1为SHOWG，字大小为48号
    Font4 = ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 48)

    # 利用text函数添加文字
    drawObject.text([200, 200], text, font=Font1)
    drawObject.text([200, 250], text, font=Font2)
    drawObject.text([200, 300], text, font=Font3)
    drawObject.text([200, 400], text, font=Font4)
    blank.show()

def creat_thumbnail(size,infile):
    im=Image.open(infile)# 创建图片对象
    im.thumbnail(size) # 缩小尺寸
    im.save("缩略图.png", "png")

def creat_message_text(text,infile):
    im = Image.open(infile)
    w, h = im.size
    # print("图片格式：%s ,图片尺寸：%s，图片RGB：%s",(im.format,(w,h),im.mode))
    Font = ImageFont.truetype("C:\Windows\Fonts\simsunb.ttf", 48)
    # 创建字体对象，吧字体设置为48号字体
    ImageDraw.Draw(im).pieslice([(w / 3 * 2, 0), (w, h / 3)], 0, 360, fill="red")
    # 绘制圆形，第一个参数界定绘制区域，宽高为原图1/3的右上角区域
    drawObject = ImageDraw.Draw(im)
    # 利用text函数添加文字
    drawObject.text((w * 0.79, h * 0.06), text, font=Font, fill='white')
    return im


if __name__=="__main__":
    infile="github_logo.png"  #图片文件
    size=(32,32)
    text=str(5)
    im3=creat_thumbnail(size,infile)
    #im3.save("缩略图.png","PNG")
    im2=creat_message_text(text,infile)  # 调用气泡函数
    im2.save("final.png","PNG")





    #im2.save("thum.png", "PNG")




import io
from django.http import HttpResponse
from PIL import Image,ImageDraw,ImageFont
import random


def verifycode(request):
    bgcolor = '#997679'
    width = 100
    height=25



    im = Image.new('RGB',(width,height),bgcolor)
    # 初始化画笔
    draw = ImageDraw.Draw(im)
    # 初始化字体
    font = ImageFont.truetype('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf',16)
    # 备选文字
    rand_str=''
    str1='ASDFGHQWERT12334'
    # 随机选出文字
    for i in range(0,6):
        rand_str+=str1[random.randrange(0,len(str1))]
    fontcolors = ['yellow','red','pink','green']
    # 写字符
    draw.text((5,3),rand_str,font=font,fill=random.sample(fontcolors,1)[0])
    # draw.text的参数，坐标，可以单独随机生成
    # 生成燥店
    fill = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    for x in range(1,100):
        xy=(random.randrange(0,width),random.randrange(0,height))
    #     定义位置(坐标)
    # 定义颜色
        fill = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        draw.point(xy,fill=fill)
    #     画点
    for y in range(1,10):
    # 画线,确认两个点
        x1= random.randrange(0,width)
        y1 = random.randrange(0,height)
        x2 = random.randrange(0, width)
        y2 = random.randrange(0, height)
        draw.line((x1,y1,x2,y2),fill=fill)
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    draw.arc((x,y,x+20,y+10),0,270,fill=fill)
    del draw
    buf = io.BytesIO()
    im.save(buf,'png')
    return  HttpResponse(buf.getvalue(),'image/png')
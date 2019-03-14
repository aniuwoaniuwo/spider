#-*-coding:utf-8-*-
#图形的验证码破解属于最简单的验证码破解
#暴力破解会耗时且容易出现莫名的错误，这里用到了tesserocr库的破解方法
import pytesseract
from PIL import Image
#不用转灰度处理和二值化处理，精度很低
def yanzm(pictruename,threshold):
    im=Image.open(pictruename)
    print(pytesseract.image_to_string(im))

    image=Image.open(pictruename)#新建一个image对象
    #image.show()
    image=image.convert('L')#进行了转灰度处理,就是转黑白
    #image.show()
    #threshold=127#阀值为127
    table=[]
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image=image.point(table,'1')#以上进行了二值化处理，值越低可能显示空白，越高月粗越模糊，最好是中间
    image.show()
    #result=tesserocr.image_to_text(image)
    result=pytesseract.image_to_string(image,lang='eng')
    print(result)
    return(result)
if __name__=='__main__':
    pictruename='code3.png'
    threshold=127
    yanzm(pictruename,threshold)
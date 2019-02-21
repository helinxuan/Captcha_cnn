# coding:utf-8
from PIL import Image
import numpy as np


# 把彩色图像转为灰度图像（色彩对识别验证码没有什么用）
def convert2gray(img):
    if len(img.shape) > 2:
        gray = np.mean(img, -1)
        # 上面的转法较快，正规转法如下
        # r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
        # gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray
    else:
        return img


# 生成字符对应的验证码
def gen_captcha_text_and_image():
    captcha_text = 'TQH2'

    # captcha = image.generate(captcha_text)
    # image.write(captcha_text, captcha_text + '.jpg')  # 写到文件

    # rm  =  'rm '+captcha_text + '.jpg'
    # print rm
    # os.system(rm)
    # time.sleep(10)

    captcha_image = Image.open('image/UserRecordAction_generateCode.jpg')
    captcha_image = np.array(captcha_image)
    return captcha_text, captcha_image


# 测试
if __name__ == '__main__':
    image = Image.open('image/UserRecordAction_generateCode.jpg')
    image = image.resize((160, 60), Image.BILINEAR)
    image = np.array(image)
    image = convert2gray(image)  # 生成一张新图
    im = Image.fromarray(image)
    im.show()

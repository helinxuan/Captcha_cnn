# coding:utf-8
from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
import matplotlib as plt
from PIL import Image
import random, requests, base64, os

plt.use('TkAgg')

# 验证码中的字符, 就不用汉字了
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


# 验证码一般都无视大小写；验证码长度4个字符
def random_captcha_text(char_set=number + ALPHABET, captcha_size=4):
    captcha_text = []
    for i in range(captcha_size):
        c = random.choice(char_set)
        captcha_text.append(c)
    return captcha_text


# 生成字符对应的验证码
def gen_captcha_text_and_image(i):
    # 读取图片文件
    imgFile, imgName = get_img_file()
    captcha_image = Image.open(imgFile[i])
    captcha_image = np.array(captcha_image)

    captcha_text = imgName[i]

    # image = ImageCaptcha(fonts=['Consolas/consola-1.ttf'])
    # captcha_text = random_captcha_text()
    # captcha_text = ''.join(captcha_text)
    # captcha = image.generate(captcha_text)

    # 生成图片与结果
    # image = ImageCaptcha()
    # captcha_text = random_captcha_text()
    # captcha_text = ''.join(captcha_text)
    # captcha = image.generate(captcha_text)
    #
    # captcha_image = Image.open(captcha)
    # captcha_image = np.array(captcha_image)
    return captcha_text, captcha_image


def get_image_text():
    appkey = '7002c85d70565436de948116ebd5738f'  # 接口申请的key
    codeType = '1004'  # 验证码的类型
    imagePath = './image/1.png'

    with open(imagePath, 'rb') as f:
        imgB64 = base64.b64encode(f.read())
        data = {
            'key': appkey,
            'codeType': codeType,
            'image': f,
            'base64Str': imgB64
        }

        r = requests.post('http://op.juhe.cn/vercode/index', data=data)
        print('r:' + r.text)


def get_img_file():
    path = "image"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    imgFile = []
    imgName = []
    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            imgFile.append(path + "/" + file)
            imgName.append(file)

    return imgFile, imgName


if __name__ == '__main__':
    get_img_file()
    gen_captcha_text_and_image(1)
    # 测试
    # while (1):
    #     text, image = gen_captcha_text_and_image()
    #     print('begin ', time.ctime(), type(image))
    #     f = plt.figure()
    #     ax = f.add_subplot(111)
    #     ax.text(0.1, 0.9, text, ha='center', va='center', transform=ax.transAxes)
    #     plt.imshow(image)
    #
    #     plt.show()
    #     print('end ', time.ctime())

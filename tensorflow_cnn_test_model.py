# coding:utf-8
from captcha_image_deal import convert2gray
from tensorflow_cnn_train import crack_captcha_cnn
from tensorflow_cnn_train import MAX_CAPTCHA
from tensorflow_cnn_train import CHAR_SET_LEN
from tensorflow_cnn_train import keep_prob
from tensorflow_cnn_train import X
from tensorflow_cnn_train import vec2text

import numpy as np
from PIL import Image
import tensorflow as tf


def crack_captcha(captcha_image):
    output = crack_captcha_cnn()

    saver = tf.train.Saver()
    with tf.Session() as sess:
        saver.restore(sess, tf.train.latest_checkpoint('.'))

        predict = tf.argmax(tf.reshape(output, [-1, MAX_CAPTCHA, CHAR_SET_LEN]), 2)
        text_list = sess.run(predict, feed_dict={X: [captcha_image], keep_prob: 1})

        text = text_list[0].tolist()
        vector = np.zeros(MAX_CAPTCHA * CHAR_SET_LEN)
        i = 0
        for n in text:
            vector[i * CHAR_SET_LEN + n] = 1
            i += 1
        return vec2text(vector)


if __name__ == '__main__':
    # text, image = gen_captcha_text_and_image()
    image = Image.open('create_image\image\code1.jpg')
    image = image.resize((160, 60), Image.BILINEAR)
    image = np.array(image)

    image = convert2gray(image)  # 把彩色图像转为灰度图像
    image = image.flatten() / 255  # 将图片一维化
    predict_text = crack_captcha(image)  # 导入模型识别
    print("正确: {}  预测: {}".format(predict_text))

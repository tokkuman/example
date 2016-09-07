# -*- coding: utf-8 -*-

import cv2
import math
import numpy as np

def otu(image):
    v = 0   # 分離度
    otu = 0   # 閾値の画素値
    image_after = image
    for t in range(1, 255, 1):  # 閾値を決定0~255まで
        w1, w2 = 0, 0   # クラス画素数
        m1, m2 = 0, 0   # クラス平均
        l1, l2 = [], []   # 画素配列
        thr = 0
        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j] < t:  # 黒
                    l1.append(image[i][j])
                else:  # 白
                    l2.append(image[i][j])
        w1, w2 = np.size(l1), np.size(l2)
        m1, m2 = np.mean(l1), np.mean(l2)
        thr = w1 * w2 * ((m1 - m2) ** 2)
    
        if thr > v:
            v = thr
            otu = t

    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] < otu:
                image_after[i][j] = 0
            else:
                image_after[i][j] = 255

    return image_after

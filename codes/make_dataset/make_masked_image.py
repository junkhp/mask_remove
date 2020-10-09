# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np


def make_masked_image(img, landmark, three_points):
    '''顔画像とランドマークからマスクをした疑似画像を生成
    input
    img:顔画像(numpyの2次元配列)
    landmark:ランドマーク(numpyの配列)
    three_points:基準となる3点(left_idx, nose_idx, right_idx)からなるtuple
    '''
    left_idx, nose_idx, right_idx = three_points

    mask_points = np.array([landmark[i] for i in list(range(left_idx-1, right_idx)) + [nose_idx-1]])

    return cv2.fillPoly(img, [mask_points], color=(255, 255, 255))

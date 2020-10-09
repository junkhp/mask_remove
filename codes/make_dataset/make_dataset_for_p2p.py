# -*- coding: utf-8 -*-
import os
import cv2
from glob import glob
from tqdm import tqdm

'''
pix2pixデータセット作成用
入力画像と正解画像を横並びに連結する
出力画像サイズ256x512
'''


def main():
    target_imgs_dir = '/disk018/share/oshiba/hackathon/datasets/ffhq_base/'
    input_imgs_dir = '/disk018/share/oshiba/hackathon/datasets/ffhq_masked_512/'
    out_dir = '/disk018/share/oshiba/hackathon/datasets/ffhq_combined/'
    img_size = 256

    input_imgs_path = sorted(glob(os.path.join(input_imgs_dir, '*.png')))
    idx = -1
    for inputp in tqdm(input_imgs_path):
        idx += 1
        if idx <= 3920:
            continue
        else:
            input_name = os.path.basename(inputp)
            target_name = input_name.replace('_masked.png', '.png')
            targetp = os.path.join(target_imgs_dir, target_name)
            out_name = input_name.replace('masked.png', 'combined.png')
            out_path = os.path.join(out_dir, out_name)
            input_img = cv2.resize(cv2.imread(inputp), (img_size, img_size))
            target_img = cv2.resize(cv2.imread(targetp), (img_size, img_size))

            out_img = cv2.hconcat([input_img, target_img])

            cv2.imwrite(out_path, out_img)


if __name__ == "__main__":
    main()

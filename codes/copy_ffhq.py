# -*- coding: utf-8 -*-
'''ffhqのデータセットをコピー'''
import os
from glob import glob
from tqdm import tqdm
import shutil


def main():
    original_dir = '/disk020/usrs/hagio/datasets/ffhq/base/'
    copy_dir = '/disk018/share/oshiba/hackathon/datasets/ffhq_base/'
    # コピーする枚数

    file_names = sorted(os.listdir(original_dir))

    print('start copy')
    for file_name in tqdm(file_names):
        original_file = os.path.join(original_dir, file_name)
        copy_file = os.path.join(copy_dir, file_name)
        shutil.copy(original_file, copy_file)


if __name__ == "__main__":
    main()

import dlib
from imutils import face_utils
import cv2
import os
from make_masked_image import make_masked_image
from glob import glob
from tqdm import tqdm
import numpy as np
import pathlib
'''
マスクの画像を作成
'''


def main():
    ffhq_base_dir = '/workspace/datasets/ffhq_base/'
    out_dir = '/workspace/datasets/ffhq_masked_512/'
    landmark_out_dir = '/workspace/datasets/ffhq_landmarks/'
    resize_size = 512

    # マスクを作るときのランドマークのインデックス
    # hackathon/landmark_sample.jpegを参照
    mask_point = (2, 29, 16)

    # 顔検出ツール,顔のランドマーク検出ツールの呼び出し
    face_detector = dlib.get_frontal_face_detector()
    predictor_path = 'shape_predictor_68_face_landmarks.dat'
    face_predictor = dlib.shape_predictor(predictor_path)

    imgs_path_list = sorted(glob(os.path.join(ffhq_base_dir, '*.png')))

    for img_path in tqdm(imgs_path_list):
        #  既に出力が存在している時にはcontinue
        img_name = os.path.basename(img_path)
        out_name = img_name.replace('.png', '_masked.png')
        out_path = os.path.join(out_dir, out_name)
        if os.path.exists(out_path):
            continue
        landmark_out_name = img_name.replace('.png', '_' + str(resize_size) + '.csv')
        landmark_out_path = os.path.join(landmark_out_dir, landmark_out_name)
        img = cv2.imread(img_path)
        # 処理高速化のためグレースケール化(任意)
        img_resized_original = cv2.resize(img, (resize_size, resize_size))
        img_gry = cv2.cvtColor(img_resized_original, cv2.COLOR_BGR2GRAY)

        # 顔検出
        # ※2番めの引数はupsampleの回数。基本的に1回で十分。
        faces = face_detector(img_gry, 1)

        if len(faces) != 1:
            continue

        face = faces[0]

        # 顔のランドマーク検出
        landmark = face_predictor(img_gry, face)
        # 処理高速化のためランドマーク群をNumPy配列に変換(必須)
        landmark = face_utils.shape_to_np(landmark)

        # マスクを描画
        masked_image = make_masked_image(img_resized_original, landmark, mask_point)

        # マスク画像保存
        cv2.imwrite(out_path, masked_image)

        # ランドマーク保存
        # pathlib.Path(landmark_out_path).touch
        np.savetxt(landmark_out_path, landmark, delimiter=',')


if __name__ == "__main__":
    main()

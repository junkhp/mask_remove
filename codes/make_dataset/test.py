import dlib
from imutils import face_utils
import cv2
import os
from make_masked_image import make_masked_image


# --------------------------------
# 1.顔ランドマーク検出の前準備
# --------------------------------
# 顔検出ツールの呼び出し
face_detector = dlib.get_frontal_face_detector()

# 顔のランドマーク検出ツールの呼び出し
predictor_path = 'shape_predictor_68_face_landmarks.dat'
face_predictor = dlib.shape_predictor(predictor_path)

# 検出対象の画像の呼び込み
img_path = 'hira.png'
print(os.path.exists(img_path))
# out_path = img_path.replace('.png', '_out.png')
out_path = 'hirabayashi_out.png'
img = cv2.imread(img_path)
# 処理高速化のためグレースケール化(任意)
img_resized_original = cv2.resize(img, (512, 512))
img_gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# リサイズ
img_resized = cv2.resize(img, (512, 512))

# --------------------------------
# 2.顔のランドマーク検出
# --------------------------------
# 顔検出
# ※2番めの引数はupsampleの回数。基本的に1回で十分。
faces = face_detector(img_resized, 1)

# 検出した全顔に対して処理
for face in faces:
    # 顔のランドマーク検出
    landmark = face_predictor(img_resized, face)
    # 処理高速化のためランドマーク群をNumPy配列に変換(必須)
    landmark = face_utils.shape_to_np(landmark)

    # ランドマーク描画
    for (i, (x, y)) in enumerate(landmark):
        cv2.circle(img_resized, (x, y), 1, (255, 0, 0), -1)

    # for i in [30, 3, 15]:
    #     cv2.circle(img_resized, (landmark[i-1][0], landmark[i-1][1]), 3, (255, 0, 0), -1)

    # マスクを描画
    masked_image = make_masked_image(img_resized_original, landmark, (2, 29, 16))


# --------------------------------
# 3.結果表示
# --------------------------------
cv2.imwrite(out_path, masked_image)
cv2.imwrite('hira_kand.png', img_resized)

# マスク除去
![生成例](https://github.com/junkhp/mask_remove//images/sample.png)
deep learningを用いてマスクをはずす

## codes
ローカル
```
/disk018/share/oshiba/hackathon/codes/
```
- ソースコード
<br>
<br>

## datasets
ローカル
```
/disk018/share/oshiba/hackathon/datasets/
```
### ffhq_base
- 人の顔画像のデータセット(70000枚)
### ffhq_landmarks
- ffhq_baseから得られた顔画像のランドマーク
### ffhq_masked_512
- ffhq_baseに疑似マスクをつけた画像
- 画像サイズ 512x512
### hirabayashi
- 平林のマスク顔のデータセット

<br>
<br>

## checkpoints
ローカル
```
/disk018/share/oshiba/hackathon/datasets/
```
- 学習済みモデル
<br>
<br>

## output
ローカル
```
/disk018/share/oshiba/hackathon/datasets/
```
- テスト結果
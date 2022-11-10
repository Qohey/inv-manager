# 環境
| 種別  |       名称       |  バージョン  | 備考  |
| :---: | :--------------: | :----------: | :---: |
|  OS   |     Windows      |      10      |       |
|  GPU  | GeForce RTX 3090 |              |       |
| CUDA  |                  |     11.3     |       |
|  lib  |     pytorch      | 1.12.1+cu113 |       |


# 環境構築
```powershell
python -m venv .env
./.env/Scripts/Activate.ps1
pip install -r requreirements.txt
```
使用したモデルは[こちら](https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5x6.pt)

他のモデルで実行したい場合は[こちら](https://github.com/ultralytics/yolov5#pretrained-checkpoints)の表のlinkから選ぶ

# 入出庫境界設定
```powershell
python set_border_rect.py
```
実行後
```python
left_late = 0
top_late = 0.4
right_late = 1
bottom_late = 1
```
の値を0-1の実数で境界にしたい位置まで設定する

# 実行
```powershell
python main.py --weights ./yolov5x6.pt --source 0
```
認識させるクラスを絞る場合は`--classes 0 5 7`のようなオプションをつける

オプション後半の数字は`./data/coco128.yaml`ファイルのnamesフィールドを参照
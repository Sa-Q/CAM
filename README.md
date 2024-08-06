<img src="https://img.shields.io/badge/PYTHON-black?style=for-the-badge&logo=python&logoColor=gold"/>
# カメラで静止画、動画を撮影する。
## 必要なもの
* Raspberry Pi 5 本体
* TKJ製作所製 ラズベリーパイ用 汎用 UI 基盤（OLED_0.91インチ）
* Raspberry Pi 公式カメラ
* カメラ用ケーブル
## 準備
* Raspberry Pi 5 本体をセットアップする
* Python venv 用ディレクトリを作成
* OLED ディスプレイ用 Python ライブラリをインストール
* OLED ディスプレイ用フォントをインストール

    mkdir V_CAM
    python -m venv --system-site-packages V_CAM
    source V_CAM/bin/activate
    
    pip3 install luma.core
    pip3 install luma.oled
    deactivate
    sudo apt-get install fonts-dejavu
    sudo apt-get install fonts-ipafont


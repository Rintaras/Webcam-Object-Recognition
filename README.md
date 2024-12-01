
# 仮想環境の作成
conda create -n py39_yolov8 python=3.9

# 仮想環境にログイン
conda activate py39_yolov8




# yolov8をclone
git clone https://github.com/ultralytics/ultralytics

# ディレクトリを移動
cd ultralytics

# 複数のライブラリを一括でインストール
pip install -r requirements.txt (pip install ultralytics transformers)

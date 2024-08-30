# ベースイメージとしてPythonを使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    # 日本語言語データをインストール
    tesseract-ocr-jpn \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Pythonの依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# TESSDATA_PREFIX環境変数を設定
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata/

# スクリプトをコンテナにコピー
COPY script.py .

# コンテナ起動時に実行するコマンド
CMD ["python", "script.py"]

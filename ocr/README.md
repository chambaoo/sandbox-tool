# ocr


### 使い方

#### 背景
Dockerfileを使用すると、ファイル変更の旅にビルドが必要になる状況のため、compose.ymlのみを使用している。
この場合、importが正しく機能しないため手動で以下を行う。

- インタープリタを起動して、以下を実行

    ```python
    python
    # 必要なモジュールは、ocr/import-script.pyに記述している
    # 以下、例
    >>> from PIL import Image
    >>> import pytesseract
    >>> exit()
    ```

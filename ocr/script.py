from PIL import Image
import pytesseract
import os

# 画像ファイルのパス
image_path = '/app/data/sample.jpeg'

# ファイルの存在確認
if not os.path.exists(image_path):
    print(f"Error: File not found at {image_path}")
    exit(1)

try:
    # 画像を開く
    image_raw = Image.open(image_path)

    # 下処理
    # トリミングする領域を指定 (left, top, right, bottom)
    img_width, img_height = image_raw.size # 864 850
    print(img_width, img_height)

    crop_w = img_width / 20
    crop_h = img_height / 40


    crop_box = (crop_w, crop_h * 6, img_width - crop_w, img_height - crop_h * 5)

    image = image_raw.convert('L').crop(crop_box)

    # グレースケール変換後の画像を保存
    image.save('/app/data/grayscale_sample.jpeg')

    # OCRでテキストとその位置情報を抽出
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    text = pytesseract.image_to_string(image, lang='jpn')

    print(data)
    print(text)

except Exception as e:
    print(f"An error occurred: {str(e)}")


# # 抽出されたデータの初期化
# n_boxes = len(data['level'])
# key_value_pairs = {}

# # キーとバリューのペアを特定するための閾値
# y_threshold = 10

# last_key = None

# for i in range(n_boxes):
#     text = data['text'][i].strip()
#     if not text:  # 空のテキストは無視
#         continue

#     x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]

#     if last_key is None:
#         last_key = text
#     else:
#         if abs(data['top'][i] - data['top'][i-1]) < y_threshold:
#             key_value_pairs[last_key] = text
#             last_key = None
#         else:
#             last_key = text

# # 結果を表示
# for key, value in key_value_pairs.items():
#     print(f"{key}: {value}")

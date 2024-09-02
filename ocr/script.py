from PIL import Image
import pytesseract
import os
import re



def getScore(target: str) -> int:
    
    # テキストを行ごとに分割し、空の行を除外
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    # 文字列「カロリー」などを探して、その次の行の位置とテキストを取得
    for i, line in enumerate(lines):
        if target in line:
            next_line_position = i + 1
            if next_line_position < len(lines):
                next_line_text = lines[next_line_position]
                # print(f"次の行の位置: {next_line_position}")
                # print(f"次の行のテキスト: {next_line_text}")
            else:
                print("次の行がありません")
            break

    match = re.search(r'(\d+)\s*/', next_line_text)
    if match:
        number_before_slash = match.group(1)
        # print(f"スラッシュの前の数字: {number_before_slash}")
        return number_before_slash


class NutritionSummary:
    calorie: int
    protein: float
    fat: float
    sugars: float
    carbohydrates: float
    dietaryFiber: float
    sodium: float

    def __init__(self, calorie: int, protein: float, fat: float, sugars: float, 
                 carbohydrates: float, dietaryFiber: float, sodium: float):
        self.calorie = calorie
        self.protein = protein
        self.fat = fat
        self.sugars = sugars
        self.carbohydrates = carbohydrates
        self.dietaryFiber = dietaryFiber
        self.sodium = sodium


    def calculateProteinBalance(self):
        return round((self.protein * 4 / self.calorie * 100), 2)

    def calculateFatBalance(self):
        return round((self.fat * 9/ self.calorie * 100), 2)
    
    def calculateCarbohydratesBalance(self):
        return round((self.carbohydrates * 4 / self.calorie * 100), 2)
    


def extractSummary(target: str) -> NutritionSummary:

    return NutritionSummary(
        calorie = 250,
        protein = 20.5,
        fat = 14.4,
        sugars = 10.3,
        carbohydrates = 40.0,
        dietaryFiber = 7.2,
        sodium = 150.0
    )


def extractSummaryErr(target: str):
    raise Exception("failed to extract summary.")

def getSumaryManually() -> NutritionSummary:
    print("calorie:")
    calorie: int = int(input())
    print("protein:")
    protein: float = float(input())
    print("fat:")
    fat: float = float(input())
    print("sugars:")
    sugars: float = float(input())
    print("carbohydrates:")
    carbohydrates: float = float(input())
    print("dietary fiber:")
    dietaryFiber: float = float(input())
    print("sodium:")
    sodium: float = float(input())

    
    return NutritionSummary(
        calorie = calorie,
        protein = protein,
        fat = fat,
        sugars = sugars,
        carbohydrates = carbohydrates,
        dietaryFiber = dietaryFiber,
        sodium = sodium,
    )

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

    # 空白を改行に置き換え
    # text = text.replace(' ', '\n')

    # # 空の行を削除
    # text_lines = text.splitlines()
    # cleaned_text = '\n'.join(line for line in text_lines if line.strip())

    # print(getScore("カロリー"))


    try:

        summary = None
        summary = extractSummaryErr(text)

    except Exception as e:
        print(f"An error occurred while extracting summary: {str(e)}")
        print("Input scores manually")
    
        try:
            summary = getSumaryManually()

        except Exception as e:
            print(f"An error occurred. Input Error: {str(e)}")

    # 計算
    print(f"P (13 ~ 20%) = {summary.calculateProteinBalance()}%")
    print(f"F (20 ~ 30%) = {summary.calculateFatBalance()}%")
    print(f"C (50 ~ 65%)= {summary.calculateCarbohydratesBalance()}%")

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

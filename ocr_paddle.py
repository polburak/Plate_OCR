# ocr_paddle.py (güncel sürüm)
import os
import pandas as pd
from paddleocr import PaddleOCR

# OCR modeli
ocr = PaddleOCR(use_textline_orientation=True, lang='en')

plate_folder = "plates"
output_csv = "plates_paddle.csv"

data = []

for image_name in os.listdir(plate_folder):
    if image_name.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(plate_folder, image_name)

        # Yeni sürümde predict() kullanılıyor
        result = ocr.predict(img_path)

        # OCR sonucu birleştir
        plate_text = " ".join([line[1][0] for page in result for line in page])
        print(f"{image_name} -> {plate_text}")

        data.append({
            "image": image_name,
            "plate": plate_text
        })

df = pd.DataFrame(data)
df.to_csv(output_csv, index=False, encoding='utf-8')
print(f"PaddleOCR sonuçları {output_csv} dosyasına kaydedildi!")

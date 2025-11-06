# ocr_paddle_only.py
import os
import cv2
import pandas as pd
from paddleocr import PaddleOCR

# PaddleOCR modeli
ocr = PaddleOCR(use_textline_orientation=True, lang='en')

plate_folder = "plates"
output_csv = "plates_paddle.csv"
data = []

for image_name in os.listdir(plate_folder):
    if image_name.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(plate_folder, image_name)
        img = cv2.imread(img_path)

        # Ön işleme
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (gray.shape[1]*3, gray.shape[0]*3))
        gray = cv2.equalizeHist(gray)
        thresh = cv2.adaptiveThreshold(gray, 255,
                                       cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY, 11, 2)

        # Tek kanalı 3 kanala çevir
        thresh_rgb = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

        # PaddleOCR
        result = ocr.predict(thresh_rgb)
        plate_text = " ".join([line[1][0] for page in result for line in page])
        print(f"{image_name} -> {plate_text}")

        data.append({
            "image": image_name,
            "plate": plate_text
        })

# CSV’ye kaydet
df = pd.DataFrame(data)
df.to_csv(output_csv, index=False, encoding='utf-8')
print(f"PaddleOCR sonuçları {output_csv} dosyasına kaydedildi!")

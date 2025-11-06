import os
import cv2
import easyocr
import pandas as pd

reader = easyocr.Reader(['en'])

plate_folder = "plates"
output_csv = "plates_easy.csv"

data = []

for image_name in os.listdir(plate_folder):
    if image_name.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(plate_folder, image_name)
        img = cv2.imread(img_path)


        result = reader.readtext(img)
        plate_text = " ".join([res[1] for res in result])
        print(f"{image_name} -> {plate_text}")

        data.append({
            "image": image_name,
            "plate": plate_text
        })

df = pd.DataFrame(data)
df.to_csv(output_csv, index=False, encoding='utf-8')
print(f"EasyOCR results saved to {output_csv} file!")

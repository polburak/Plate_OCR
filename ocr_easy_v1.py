import os
import cv2
import numpy as np
import easyocr

reader = easyocr.Reader(['en'])
plate_folder = "plates"
output_folder = "plates_labeled"
os.makedirs(output_folder, exist_ok=True)

for image_name in os.listdir(plate_folder):
    if image_name.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(plate_folder, image_name)
        img = cv2.imread(img_path)

        # OCR
        result = reader.readtext(img)
        text = " ".join([r[1] for r in result])
        print(f"{image_name} -> {text}")


        h, w, c = img.shape
        blank_space = np.ones((h, w, c), dtype=np.uint8) * 255
        labeled_img = np.hstack((img, blank_space))


        cv2.putText(labeled_img, text, (w + 10, h // 2), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 0), 2, cv2.LINE_AA)


        output_path = os.path.join(output_folder, image_name)
        cv2.imwrite(output_path, labeled_img)

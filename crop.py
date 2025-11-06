import os
import cv2
from ultralytics import YOLO

model = YOLO("best.pt")

input_folder = "output"
plate_folder = "plates"
os.makedirs(plate_folder, exist_ok=True)

for image_name in os.listdir(input_folder):
    if image_name.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(input_folder, image_name)
        img = cv2.imread(img_path)

        results = model.predict(source=img, conf=0.5)

        for result in results:
            for idx, box in enumerate(result.boxes):
                cls_id = int(box.cls[0])
                if cls_id == 0:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    plate_img = img[y1:y2, x1:x2]

                    plate_img = cv2.resize(plate_img, (plate_img.shape[1]*3, plate_img.shape[0]*3))

                    plate_filename = f"{os.path.splitext(image_name)[0]}_plate{idx}.png"
                    cv2.imwrite(os.path.join(plate_folder, plate_filename), plate_img)
                    print(f"{plate_filename} recorded.")

print("All plates were cropped and recorded!")

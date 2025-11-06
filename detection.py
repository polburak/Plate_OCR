from ultralytics import YOLO
import cv2
import os


model = YOLO("best.pt")

image_folder = "data"
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)


for image_name in os.listdir(image_folder):
    if image_name.lower().endswith((".png", ".jpg", ".jpeg")):
        image_path = os.path.join(image_folder, image_name)
        img = cv2.imread(image_path)

        results = model.predict(source=img, conf=0.5)

        for result in results:
            boxes = result.boxes
            for box in boxes:
                cls_id = int(box.cls[0])

                if cls_id == 0:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(img, "Plate", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)


        output_path = os.path.join(output_folder, image_name)
        cv2.imwrite(output_path, img)
        print(f"{image_name} processed and recorded.")

print("All images have been processed!")

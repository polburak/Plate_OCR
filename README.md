#  License Plate Recognition Project

A simple Python + EasyOCR / PaddleOCR project for detecting and reading vehicle license plates from images. Results are saved as labeled images and can also be exported to a CSV.

---

## 🚀 Features

- Detect vehicles and license plates using YOLO (detection.py)
- Crop detected plates (crop.py)
- OCR for reading license plate numbers using EasyOCR (ocr_easy_v1.py)
- Optional OCR using PaddleOCR for experimentation
- Writes recognized plate text on images in plates_labeled/
- Saves OCR results to a CSV (plates_paddle.csv or plates_easy.csv)
- Preprocessing for better OCR accuracy (resize, grayscale, thresholding)

---

## 🖼️ Screenshots

![License Plate OCR](plates_labeled/car(1)_plate0.png)


---

## 📝 Notes

1. OCR may occasionally misread characters.
2. YOLO model (best.pt) should be placed in the project root or configured path.
3. For best results, images should be clear, well-lit, and plates visible.
4. Large folders like plates/ or output/ can be added to .gitignore to avoid committing images to GitHub. 


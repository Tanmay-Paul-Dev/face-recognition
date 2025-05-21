# 🧠 Face Matcher

A Python script that scans a folder of images, detects faces, and copies the ones that contain a face matching a reference photo to an output folder.

Perfect for sorting group photos or surveillance footage based on a known person’s face.

---

## 📂 How It Works

1. You provide:
   - A folder of input images
   - A reference image (the face you're looking for)
2. The script detects all faces in each image using `face_recognition`.
3. If any face in an image matches the reference face:
   - That image is **copied** to the output folder.

---

## ✅ Requirements

- Python 3.11
- Dependencies (install via pip):


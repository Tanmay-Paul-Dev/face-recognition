import os
import shutil
from pathlib import Path
from PIL import Image
import face_recognition
import cv2


def is_image_file(file_path):
    """Check if the file is a valid image based on extension and actual readability."""
    try:
        Image.open(file_path).verify()
        return file_path.lower().endswith(('.png', '.jpg', '.jpeg'))
    except:
        return False


def get_face_encodings(image_path, model="hog", resize_scale=0.5):
    """Load image, resize for performance, and return face encodings."""
    try:
        # Load and resize
        image = face_recognition.load_image_file(image_path)
        if resize_scale != 1.0:
            image = cv2.resize(image, (0, 0), fx=resize_scale, fy=resize_scale)

        # Extract encodings
        return face_recognition.face_encodings(image, model=model)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return []


def process_images(input_folder, reference_photo, output_folder, tolerance=0.6, model="hog"):
    """Compare each image in folder with reference, and move matched ones to output folder."""
    # Create output folder
    Path(output_folder).mkdir(exist_ok=True)

    # Load reference encoding
    print(f"\nEncoding reference face: {reference_photo}")
    ref_encodings = get_face_encodings(reference_photo, model=model)
    if not ref_encodings:
        print("❌ No face found in reference image.")
        return
    reference_encoding = ref_encodings[0]

    # Collect valid image files
    image_files = [
        f for f in os.listdir(input_folder)
        if is_image_file(os.path.join(input_folder, f))
    ]

    print(f"\n📂 Found {len(image_files)} valid image(s) to process.\n")

    # Loop through images
    for idx, filename in enumerate(image_files, 1):
        filepath = os.path.join(input_folder, filename)
        print(f"[{idx}/{len(image_files)}] Processing: {filename}")

        encodings = get_face_encodings(filepath, model=model)
        if not encodings:
            print("   ⚠️ No faces detected.")
            continue

        # Compare all detected faces
        print(f"   👥 {len(encodings)} face(s) detected.")
        matches = face_recognition.compare_faces(encodings, reference_encoding, tolerance=tolerance)
        if any(matches):
            dest_path = os.path.join(output_folder, filename)
            shutil.copy2(filepath, dest_path)
            print("   ✅ Match found. Moved to output folder.")
        else:
            print("   ❌ No match.")

    print("\n✅ Done.")


def main():
    input_folder = "input_photos"          # Folder with images
    reference_photo = "reference.jpg"      # Reference image path
    output_folder = "alok_matched_photos_v2"       # Destination for matches
    tolerance = 0.5                         # Face match tolerance (lower = stricter)
    model = "cnn"                           # "hog" = fast (CPU), "cnn" = accurate (GPU)

    if not os.path.exists(input_folder):
        print(f"❌ Input folder '{input_folder}' not found.")
        return
    if not os.path.exists(reference_photo):
        print(f"❌ Reference photo '{reference_photo}' not found.")
        return

    process_images(input_folder, reference_photo, output_folder, tolerance, model)


if __name__ == "__main__":
    main()

import os
from PIL import Image

# Tự lấy folder chứa file .py
input_folder = os.path.dirname(os.path.abspath(__file__))

# Detect tất cả file ảnh
image_exts = {".jpg", ".jpeg", ".bmp", ".webp", ".tiff", ".tif", ".gif", ".png"}

for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    if os.path.isfile(file_path):
        ext = os.path.splitext(filename)[1].lower()

        if ext in image_exts:
            try:
                img = Image.open(file_path)

                # Convert mode chuẩn
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGBA")
                else:
                    img = img.convert("RGB")

                # Luôn save đè thành PNG
                new_name = os.path.splitext(filename)[0] + ".png"
                output_path = os.path.join(input_folder, new_name)

                img.save(output_path, "PNG")
                print(f"Converted: {filename} -> {new_name}")

            except Exception as e:
                print(f"Error converting {filename}: {e}")

print("Done!")
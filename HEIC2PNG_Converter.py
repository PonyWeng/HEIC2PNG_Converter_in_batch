import os
from heic2png import HEIC2PNG

def convert_and_delete_heic(heic_file_path, quality=90):
    try:
        heic_img = HEIC2PNG(heic_file_path, quality=quality)
        png_file_path = os.path.splitext(heic_file_path)[0] + '.png'
        heic_img.save(png_file_path)
        # os.remove(heic_file_path)  # !!!! Delete original HEIC file !!!
        print(f"Converted and deleted {heic_file_path}, saved as {png_file_path}")
    except Exception as e:
        print(f"Error converting {heic_file_path}: {e}")

def batch_convert_and_delete_heic(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".heic"):
            heic_file_path = os.path.join(folder_path, filename)
            convert_and_delete_heic(heic_file_path)

# Specify the path that contains the HEIC file.
folder_path = 'yourpath' 

print("Start Converting...")
batch_convert_and_delete_heic(folder_path)

import os
from heic2png import HEIC2PNG

def convert_and_delete_heic(heic_file_path, output_folder, quality=90):
    try:
        heic_img = HEIC2PNG(heic_file_path, quality=quality)
        filename = os.path.splitext(os.path.basename(heic_file_path))[0] + '.png'
        png_file_path = os.path.join(output_folder, filename)
        heic_img.save(png_file_path)
        # os.remove(heic_file_path)  # !!!! Delete original HEIC file !!!
        print(f"Converted {heic_file_path}, saved as {png_file_path}")
    except Exception as e:
        print(f"Error converting {heic_file_path}: {e}")

def batch_convert_and_delete_heic(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            heic_file_path = os.path.join(input_folder, filename)
            convert_and_delete_heic(heic_file_path, output_folder)

# 輸入與輸出目錄
input_folder = 'input_images'
output_folder = 'output_images'

print("Start Converting...")
batch_convert_and_delete_heic(input_folder, output_folder)
import os
from PIL import Image

def convert_images_to_jpg(input_dir, output_dir):
    for root, _, files in os.walk(input_dir):
        for file in files:
            ext = file.lower().split('.')[-1]
            if ext == 'png':
                input_path = os.path.join(root, file)
                # 保持原資料夾結構
                relative_path = os.path.relpath(root, input_dir)
                output_folder = os.path.join(output_dir, relative_path)
                os.makedirs(output_folder, exist_ok=True)
                # 輸出檔名改成 .jpg
                output_file = os.path.splitext(file)[0] + ".jpg"
                output_path = os.path.join(output_folder, output_file)
                
                try:
                    with Image.open(input_path) as img:
                        # 直接轉換為RGB模式（忽略透明通道）
                        if img.mode != 'RGB':
                            img = img.convert('RGB')
                        
                        # 保存為JPG格式
                        img.save(output_path, "JPEG", quality=95)
                    print(f"Converted: {input_path} -> {output_path}")
                except Exception as e:
                    print(f"Failed to convert {input_path}: {e}")

# 使用方式
input_folder = r"./public/images"
output_folder = r"./public/images"
convert_images_to_jpg(input_folder, output_folder)
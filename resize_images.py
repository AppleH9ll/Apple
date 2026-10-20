from PIL import Image
import os

input_folder = "proverka_raw_images"  # Папка с исходниками
output_folder = "proverka_dataset"    # Папка для Label Studio
target_size = (640, 640)     # Единый размер

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert("RGB") # Конвертация в RGB
        img = img.resize(target_size)              # Изменение размера
        img.save(os.path.join(output_folder, filename), "JPEG") # Сохранение
print("Готово! Все фото приведены к формату 640x640.")
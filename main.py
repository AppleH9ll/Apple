import os
import time
import argparse
from PIL import Image
from multiprocessing import Pool
import random

INPUT_DIR = "input_images"
OUTPUT_DIR = "processed"
OUT_PREFIX = "out_"
TARGET_SIZE = (800, 600)
NUM_IMAGES = 10

def generate_test_images(num=NUM_IMAGES):
    """Генерирует случайные JPG-изображения в папку INPUT_DIR."""
    os.makedirs(INPUT_DIR, exist_ok=True)
    existing = len([f for f in os.listdir(INPUT_DIR) if f.endswith(".jpg")])
    if existing >= num:
        print(f"Найдено {existing} изображений. Генерация не требуется.")
        return
    print(f"Генерация {num} тестовых изображений...")
    for i in range(num):
        width = random.randint(300, 2000)
        height = random.randint(300, 2000)
        img = Image.new("RGB", (width, height))
        pixels = img.load()
        for x in range(width):
            for y in range(height):
                pixels[x, y] = (random.randint(0, 255),
                                random.randint(0, 255),
                                random.randint(0, 255))
        img.save(os.path.join(INPUT_DIR, f"img_{i}.jpg"))
    print("Генерация завершена.")

def process_image(img_info):
    """Принимает (input_path, output_path) и выполняет обработку."""
    input_path, output_path = img_info
    try:
        with Image.open(input_path) as img:
            img = img.transpose(Image.ROTATE_90)
            img = img.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
            img = img.convert("L")
            img.save(output_path, "JPEG")
        return True
    except Exception as e:
        print(f"Ошибка при обработке {input_path}: {e}")
        return False

def sequential_processing(image_files):
    """Последовательная обработка."""
    start_time = time.time()
    for input_path, output_path in image_files:
        process_image((input_path, output_path))
    elapsed = time.time() - start_time
    return elapsed

def parallel_processing(image_files, num_workers=None):
    """Параллельная обработка с использованием multiprocessing.Pool."""
    start_time = time.time()
    with Pool(processes=num_workers) as pool:
        pool.map(process_image, image_files)
    elapsed = time.time() - start_time
    return elapsed

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["sequential", "parallel"], required=True,
                        help="Режим обработки: sequential или parallel")
    args = parser.parse_args()

    generate_test_images()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    image_files = []
    for filename in sorted(os.listdir(INPUT_DIR)):
        if filename.lower().endswith(".jpg"):
            input_path = os.path.join(INPUT_DIR, filename)
            out_name = OUT_PREFIX + filename
            output_path = os.path.join(OUTPUT_DIR, out_name)
            image_files.append((input_path, output_path))

    if not image_files:
        print("Нет изображений для обработки.")
        return

    print(f"Найдено {len(image_files)} изображений.")

    if args.mode == "sequential":
        elapsed = sequential_processing(image_files)
        print(f"Последовательная обработка: {elapsed:.4f} секунд")
    else:
        elapsed = parallel_processing(image_files)
        print(f"Параллельная обработка (multiprocessing.Pool): {elapsed:.4f} секунд")

if __name__ == "__main__":
    main()

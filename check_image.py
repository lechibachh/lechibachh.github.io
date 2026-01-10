from PIL import Image
import os

try:
    img = Image.open('assets/img/favicon.jpg')
    print(f"Format: {img.format}")
    print(f"Mode: {img.mode}")
    print(f"Size: {img.size}")
except Exception as e:
    print(f"Error: {e}")

# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python
# pip install pillow
from pathlib import Path

from PIL import Image

ROOT_FOLDER = Path(__file__).parent
ORIGINAL_IMAGE = ROOT_FOLDER / 'original.JPG'
NEW_IMAGE = ROOT_FOLDER / 'new_image.JPG'

pil_image = Image.open(ORIGINAL_IMAGE)
widht, height = pil_image.size
exif = pil_image.info['exif']  # Mantém as informações da imagem

# width     new_width
# height    ??
new_width = 640
new_height = round(height * new_width / widht)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    exif=exif,
)

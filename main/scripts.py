from pathlib import Path
import os
from main.models import Photo
from PIL import Image
from django.core.files import File

def load_images(folder_path):
    files = Path(folder_path).iterdir()
    for _file in files:
        if is_image(_file):
            name = str(_file).split('/')[-1]
            image = Image.open(_file)
            p1 = Photo.objects.create()
            p1.name = name
            p1.image.save(name, File(open(str(_file), 'rb')))
            # p1.image.save(str(_file), File(open(str(_file), 'rb')))
            p1.save()


def is_image(file_path):
    try:
        im=Image.open(file_path)
        return True
    except IOError:
        return False
from PIL import Image
from PIL import ImageOps
import os


DIR = 'C:/Users/Admin/Documents/BISU files per sem/Year 4, Sem 1/Thesis/test_steno_ocr/dataset/train/'
OUT_DIR = 'C:/Users/Admin/Documents/BISU files per sem/Year 4, Sem 1/Thesis/fix size of train data (python processed)/'
FILENAME = os.listdir(DIR)
NEW_H = 30
NEW_W = 30


for file_name in FILENAME:
    img = Image.open(DIR + file_name, 'r')
    img = ImageOps.contain(img, (NEW_W, NEW_H))
    img_w, img_h = img.size
    background = Image.new('RGBA', (NEW_W, NEW_H), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img, offset)
    background.save(OUT_DIR + file_name)



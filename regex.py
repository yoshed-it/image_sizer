import re, os


filenames = [
    "123x456",
    "123x456_1a",
    "78x90-2B",
    "56x78",
    "12x34_3c",
    ".DS_Store",
    "katenet-pinkflowerwallpaper2011_1024x1024.jpg",
    "marble-1k.jpeg",
    "resized_images",
    "test-button-1024x1024.png",
    "picture_08_1024x768.jpg"
]


pattern = re.compile("([_-]?\d+x\d+)|\d+[Kk]")


for files in filenames:
    
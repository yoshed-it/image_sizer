"""
Let's say I have a folder with these images in it, they are all 1k in size (1024x1024). I'd like a command line tool that would allow me to specify a size and convert all the images in the folder to said size using linear scaling(also called Nearest Neighbor).

So rock_wall_08_ao_1k.png would become rock_wall_08_ao_256.png if I choose 256 as the scale.

The images will always have the same width and height, so it only needs to take in a single number.


The way to start:

TODO: Get Image Object from Pillow and resize from user input
TODO: Ask for folder path, read all IMAGES in the file and resize. Use OS?
Should I create a copy of the image, create a new folder and then save the edited images in the new folder?
Maybe just have that as an option.
TODO: Store images in an array or dict or tuple so that they can be looped over ie:
TODO: Error Handling
TODO: After resizing the image, get the name, and rename the image. EX rock_wall_08_ao_1k.png would become rock_wall_08_ao_256.png if I choose 256 as the scale.

osFunction() -- Does thing, gets info about what is inside the file
for images in range(0, fileSize)
    append arrOfImages = [blah, blah, blah.jpg]
    do something
TODO: Stretch goal --> add a simple GUI, image options, some option to fuck with tyler.
TODO: Add to PATH: adding the script’s directory to your PATH environment variable allows you to run the script from anywhere.
TODO: Use File-like files to resize images in memory, and provide a ticker or loader or something fancy like...

||||||||||||||||||||| pipes to show loading
Program Exited in 3s after processing n images.
"""

from PIL import Image
import os

current_directory = os.getcwd()
# current_directory_contents = os.listdir('images')

# Get files in whatever directory the images are stored in.
# TODO use add to PATH to get the cwd and runt he script globaly


image_store = []
for files in os.listdir('images'):
    image_store.append(os.path.join('images', files))




def resize_image():
    size = 256, 256
    os.makedirs(name='Resized Images')
    for images in image_store:
        resized_images = os.path.splitext(images)[0] + "-256.png"
        if images != resized_images:
            try:
                with Image.open(images) as im:
                    im.resize(size, Image.Resampling.NEAREST)
                    im.save(resized_images, "PNG")
                    print(images, im.format, f"{im.size}")
                    return images
            except OSError:
                pass

def make_dir():
    os.makedirs(name="Resized Images")

# resize_image()
make_dir()
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


"""

EXAMPLE FOR DIRECTORY MANAGEMENT
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Resize images in a directory.")
    parser.add_argument('directory', type=str, help="Directory containing images to resize.")
    parser.add_argument('new_size', type=int, help="New size for the images (e.g., 256 for 256x256).")
    parser.add_argument('--output', type=str, help="Optional: Output directory for resized images.", default=None)
    return parser.parse_args()

args = get_args()
print(f"Resizing images in {args.directory} to {args.new_size}x{args.new_size}")
if args.output:
    print(f"Saving resized images to {args.output}")
"""


from PIL import Image
import os, re, time

#current_directory = os.getcwd()
# current_directory_contents = os.listdir('images')

# Get files in whatever directory the images are stored in.
# TODO use add to PATH to get the cwd and run the script globaly
# TODO Add in the "do doop, doo doop" noise

def main():
    pass


def get_user_directory():
    while True:
        get_dir = input("What directory are we pulling from?   \n(type 'exit' to quit)")
        if get_dir.lower() == 'exit':
            print("Exiting Program")
            time.sleep(3)
            return None
        if os.path.exists(get_dir):
            print(f"Images in {get_dir} will be resized.")
            return get_dir
        else: print(f"{get_dir} does not exist")
        return None
        

def get_user_img_size():
    while True:   
        get_img_size = input("What Size Square are we Makin'?   ")
        if get_img_size:
            try: 
                validated_image_size = int(get_img_size)
                return validated_image_size
            except ValueError: 
                print("Please provide a valid number")
        

def get_user_input():   # Break into multiple functions
    print("Welcome to WONKY: The Image Resizing Tool....\nLets Resize Some Images 'Yall!")
    image_directory = get_user_directory()
    if image_directory is not None:
        img_size = get_user_img_size()
        return image_directory, img_size
    else:
        return None, None
     
    

image_store = []
for files in os.listdir('images'):
    image_store.append(os.path.join('images', files))

print("Image Store Array", image_store)


# def resize_image():
#     new_image_size = (256, 256)
#     for images in image_store:
#         image_output_filename = os.path.splitext(images)[0] + "-256.png"
#         if images != image_output_filename and Image.Image.size != :
#             try:
#                 with Image.open(images) as im:
#                     image_resizing_action = im.resize(size=new_image_size, resample=Image.Resampling.NEAREST)
#                     image_resizing_action.save(image_output_filename, "PNG")
#                     print(image_output_filename, im.format, f"{im.size}")

#             except OSError:
#                 pass


# def make_dir():
#     os.makedirs(name="Resized Images")

# resize_image()
# make_dir()
get_user_input()
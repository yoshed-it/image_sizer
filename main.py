from PIL import Image
import os
from user_input import UserInput

"""



Should I create a copy of the image, create a new folder and then save the edited images in the new folder?
Maybe just have that as an option.
TODO: Store images in an array or dict or tuple so that they can be looped over ie:
TODO: After resizing the image, get the name, and rename the image. EX rock_wall_08_ao_1k.png would become rock_wall_08_ao_256.png if I choose 256 as the scale.


TODO: Stretch goal --> add a simple GUI, image options, some option to fuck with tyler.
TODO: Add to PATH: adding the script’s directory to your PATH environment variable allows you to run the script from anywhere.
TODO: Use File-like files to resize images in memory, and provide a ticker or loader or something fancy like...

||||||||||||||||||||| pipes to show loading
Program Exited in 3s after processing n images.
"""



# current_directory = os.getcwd()
# current_directory_contents = os.listdir('images')

# Get files in whatever directory the images are stored in.
# TODO use add to PATH to get the cwd and run the script globaly
# TODO Add in the "do doop, doo doop" noise


def main():
    print("Im here in main! main()")  # Check entry
    user_input = UserInput()
    if user_input.get_user_input():
        print("Valid input received, proceeding with resizing.")  # Check input validity
        resize_image(user_input.source_directory, user_input.image_size)
        make_new_image_directory_and_save(user_input.source_directory)
    else:
        print("Invalid input, terminating program.")  # Check input failure


def make_new_image_directory_and_save(source_directory):
    new_directory = "resized_images"
    try:
        print(f"File Path: {new_directory}")
        os.mkdir(path=new_directory, exist_ok=True)
        return new_directory
    except FileExistsError:
        print(f"The directory {source_directory} already exists.")
    except OSError as error:
        print(f"An error occurred while creating the directory: {error}")


def resize_image(source_directory, image_size):
    new_directory_path = make_new_image_directory_and_save(source_directory)
    image_store = [os.path.join(source_directory, image_file) for image_file in os.listdir(source_directory)]
    for image_path in image_store:
        file_name, ext = os.path.splitext(image_path)
        image_output_filename = f"{file_name}_{image_size}{ext}"
        new_image_size = image_size, image_size
        if image_path != image_output_filename:
            try:
                with Image.open(image_path) as im:
                    resized_image = im.resize(new_image_size, Image.Resampling.NEAREST)
                    resized_image.save(image_output_filename)
                    print(image_output_filename)
            except OSError as error:
                print(f"couldn't process {image_path}, {error}")


if __name__ == "__main__":
    main()
    print("hello")

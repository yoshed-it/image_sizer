from PIL import Image
import os
from user_input import UserInput

# current_directory = os.getcwd()
# current_directory_contents = os.listdir('images')

# Get files in whatever directory the images are stored in.
# TODO use add to PATH to get the cwd and run the script globaly
# TODO Add in the "do doop, doo doop" noise

user_input = UserInput()

def main():
    if user_input.get_user_input():
        print("Valid input received, proceeding with resizing.")  # Check input validity
        make_new_image_directory_and_save()
        resize_image(user_input.source_directory, user_input.image_size)
    else:
        print("Invalid input, terminating program.")  # Check input failure


def make_new_image_directory_and_save():
    new_directory = os.path.join(user_input.source_directory, "resized_images")
    try:
        print(f"Resized images can be found in:{new_directory}")
        os.makedirs(name=new_directory, exist_ok=True)
        return new_directory
    except OSError as error:
        print(f"An error occurred while creating the directory: {error}")


def is_valid_image_extension(file_name):  # Checks to make sure the image is ACTUALLY an image
    valid_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
    return any(file_name.lower().endswith(ext) for ext in valid_extensions)


def resize_image(source_directory, image_size):
    new_directory_path = make_new_image_directory_and_save()
    image_store = [os.path.join(source_directory, image_file)
                   for image_file in os.listdir(source_directory)
                   if os.path.isfile(os.path.join(source_directory, image_file))
                   and is_valid_image_extension(image_file)]

    for image_path in image_store:
        base_name = os.path.basename(image_path)
        file_name, ext = os.path.splitext(base_name)
        image_output_filename = f"{file_name}_{image_size}{ext}"
        new_image_size = image_size, image_size

        if image_path != image_output_filename:
            try:
                with Image.open(image_path) as im:
                    resized_image = im.resize(new_image_size, Image.NEAREST)
                    new_file_path = os.path.join(new_directory_path, image_output_filename)
                    resized_image.save(new_file_path)
                    print("Image saved:", new_file_path)
            except OSError as error:
                print(f"couldn't process {image_path}, {error}")


# THIS DOESN'T WORK IN THE FUCKING WAY I WANT AND I WILL BURN EVERYTHING DOWN

if __name__ == "__main__":
    main()

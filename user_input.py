import os


class UserInput:
    def __init__(self):
        self.source_directory = None
        self.image_size = None

    def get_user_directory(self):
        while True:
            get_directory = input("In what directory are the images located?   \n(type 'exit' to quit)")
            if get_directory.lower() == 'exit':
                print("Exiting Program")
                return False
            if os.path.exists(get_directory):
                print(f"Images in {get_directory} will be resized.")
                self.source_directory = get_directory
                return True
            else:
                print(f"{get_directory} does not exist")

    def get_user_img_size(self):
        while True:
            get_img_size = input("What ill be the new image size??   ")
            try:
                validated_image_size = int(get_img_size)
                if validated_image_size > 0:
                    self.image_size = validated_image_size
                    return True
            except ValueError:
                print("Please provide a valid number")

    def get_user_input(self):
        if self.get_user_directory() and self.get_user_img_size():
            return True
        return False

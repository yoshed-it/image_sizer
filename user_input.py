import os
import simpleaudio as sa
import time

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
            get_img_size = input("What will be the new image size(please enter only a number of pixels)?   ")
            try:
                validated_image_size = int(get_img_size)
                if validated_image_size > 0:
                    self.image_size = validated_image_size
                    return True
            except ValueError:
                print("Please provide a valid number")
                
    def sound_on(self):
        while True:
            ask_for_sound = input("Would you like Sound with That? (yes/no): ")
            if ask_for_sound.lower() in ['n', 'no']:
                print("Continuing with image resizing")
                return False
            elif ask_for_sound.lower() in ['y', 'yes']:
                sound_file = "printer.wav"
                if os.path.exists(sound_file):
                    wave_obj = sa.WaveObject.from_wave_file(sound_file)
                    wave_obj.play()  # Start playing the sound
                    time.sleep(7)
                    return True
                else:
                    print("Please enter 'yes' or 'no'.")
                
        
        
    def get_user_input(self):
        if self.get_user_directory() and self.get_user_img_size():
            return True
        return False

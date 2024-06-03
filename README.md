# Image Sizer
Simple CLI tool for image resizing

## Dependencies:
- Pillow: 10.3.0

## How to Run:
1. Navigate to the script directory.
2. Run the script with one of the following commands, depending on your pip version:
    ```sh
    pip main.py
    pip3 main.py
    ```

The script will prompt you to provide a direct path (not a relative path) to a directory containing images. Non-image files will be ignored. You will then be prompted to provide a single dimension (an integer representing one side of a square, without the 'pixels' suffix).

The image extension will remain the same as the original extension.

Once run, the resized images will be copied into a new folder named `Resized_Images` within the original image directory. Images will be renamed from `hi_im_an_image-1024x1024.jpg` or `im_also_an_image1k.png` to `hi_im_an_image_SIZEOFNEWIMAGE.jpg` or `im_also_an_image_SIZEOFNEWIMAGE.png`.

## TODO:
- Add support for system arguments.
- Allow images to be saved to a specified directory.

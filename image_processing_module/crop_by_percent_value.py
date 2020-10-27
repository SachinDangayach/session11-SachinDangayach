# crop_by_percent_value.py

import os
from PIL import Image
import argparse

# TODO: 4.2 centre square/rectangle crop by user-determined percentage (crop to 50%/70%) crp_p
def crop_by_percent(w_percent, h_percent, source, destination):
    """
    crop the image by given pixels precentage
    usage: crop_by_percent_value.py [-w --wdth] [-h --hgth] [-s --src] [-d --dest] [-h --help]

    # Inputs:
        w_pixel : percent of width, images width will be cropped
        h_pixel : pecent of height, images height will be cropped
        source : path to the folder containing images
        destination : path to the folder to place resize images

    # Functionality :
        Takes all images in the given source and crop as per given perecent
        values of width and height
        for example, the image is of size 100 X 100 and pixel values are w_pixel = 10%
        and h_pixel = 20%, new size of the image will be 90 X 80 cropped from center
    """

    # Validations
    if source == None or source == '':
        raise ValueError(f"Invalid Source")

    if not isinstance(source, str):
        raise ValueError(f"Invalid Source {source}")

    if not os.path.isdir(source):
        raise ValueError(f"Source {source} has to be folder path")

    if (destination == '' or destination == None) and os.path.isdir(source): # source and destination are same folders
        destination = source

    if not os.path.isdir(destination):
        raise ValueError(f"Destination {destination} in not a folder path")

    if not isinstance(w_percent, int):
        raise ValueError(f"Invalid Source {w_percent}")

    if w_percent <= 0 and w_percent<100:
        raise ValueError(f"Width percentage value should be greater than 0 and less than 100")

    if not isinstance(h_percent, int):
        raise ValueError(f"Invalid Source {h_percent}")

    if h_percent <= 0 and w_percent<100:
        raise ValueError(f"Height percentage value should be greater than 0 and less than 100")

    cropped_files = []
    failed_files = []

    filenames = os.listdir(source)

    for fl in filenames:
        file, extension = os.path.splitext(fl)
        if extension not in {'.png','.jpeg','.jpg'}: # Check for image files in folder
            print(f"Can't crop {fl}")
            failed_files.append(fl)
            continue
        try:
            img = Image.open(os.path.join(source, fl))
            w, h = img.size # Get size of image
            if w_percent > 100 or h_percent >100:
                print(f"Image {fl} can't be cropped more than 100% of its size")
                img.close()
                failed_files.append(fl)
                continue

            w_pixel = int(w*w_percent/100)
            h_pixel = int(h*h_percent/100)

            # Setting the points for cropped image
            left = int(w/2 - w_pixel/2)
            top =  int(h/2 - h_pixel/2)
            right = int(left + w_pixel)
            bottom = int(top + h_pixel)

            # Cropped image of above dimension
            # (It will not change orginal image)
            img = img.crop((left, top, right, bottom))

            img.save(os.path.join(destination, fl))
            img.close()
            cropped_files.append(fl)
            print(f'Image {fl} cropped successfully')
        except OSError:
            print(f'Cannot resize image')
        # For permission related errors
        except PermissionError:
            print("Operation not permitted.")

    if len(failed_files) == len(filenames):
        print(f'no files to resize')
        return True
    elif len(cropped_files) > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(f'Loading from command line crop_by_percent_value.py: __name__ = {__name__}')

    # get code, source, destination, recentage from arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-w', '--width', type= int, help='Enter the % value of width to be center cropped')
    parser.add_argument('-ht', '--height', type= int, help='Enter the % value of height to be center cropped')
    parser.add_argument('-s', '--src', type= str, help='Enter the absolute path of input folder')
    parser.add_argument('-d', '--dest', type= str, help='Enter the absolute path of output folder')

    args = parser.parse_args()

    if args.src is not None and args.width is not None and args.height is not None:
        crop_by_percent(w_percent = args.width, h_percent = args.height, source = args.src, destination = args.dest)
    else:
        print('Invalid arguments passed, please check help')

else:
    print(f'Loading crop_by_percent_value.py: __name__ = {__name__}')

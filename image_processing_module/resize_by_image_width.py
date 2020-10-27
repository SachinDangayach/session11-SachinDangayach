# resize_by_image_width.py

import os
from PIL import Image
import argparse

# TODO: 3.2 resize by user determined width (proportional) res_w
def resize_by_width(new_width, source, destination=''):
    """
    Resize all images in proportion in a given folder by user defined width
    usage: resize_by_width.py [-w --wdth] [-s --src] [-d --dest] [-h --help]

    # Inputs:
        new_width : new width to which images will be resized.
                    height will be adjusted in proportion
        source : path to the folder containing images
        destination : path to the folder to place resize images

    # Functionality :
        Takes all images in the given source and resize as per give width
        for example if image is of size 100 X 100 and new width is 120, then
        the new heigh to maintain the proportion will be 120, then all images
        will be resized to 120 X 120
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

    if not isinstance(new_width, int):
        raise ValueError(f"Invalid Source {new_width}")

    if new_width <= 0:
        raise ValueError(f"Width value should be greater than 0")

    resized_files = []
    failed_files = []

    filenames = os.listdir(source)

    for fl in filenames:
        file, extension = os.path.splitext(fl)
        if extension not in {'.png','.jpeg','.jpg'}: # Check for image files in folder
            print(f"Can't resize {fl}")
            failed_files.append(fl)
            continue
        try:
            img = Image.open(os.path.join(source, fl))
            w, h = img.size # Get size of image
            resize_factor = new_width/w # Calculate resizing factor
            w_new,h_new = int(new_width),int(h*resize_factor)
            if resize_factor < 1: # Downsample
                img = img.resize((w_new,h_new),Image.ANTIALIAS)
                img.save(os.path.join(destination, fl))
                img.close()
                resized_files.append(fl)
                print(fl, w_new,h_new)
            else: # Upsample
                img = img.resize((w_new,h_new),Image.BILINEAR)
                img.save(os.path.join(destination, fl))
                img.close()
                resized_files.append(fl)
                print(fl, w_new,h_new)
        except OSError:
            print(f'Cannot resize image')

        # If source or destination is not a valid directory
        except NotADirectoryError:
            print("Source is a directory but destination is a file.")

        # For permission related errors
        except PermissionError:
            print("Operation not permitted.")

    if len(failed_files) == len(filenames):
        print(f'no files to resize')
        return True
    elif len(resized_files) > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(f'Loading from command line resize_by_image_width.py: __name__ = {__name__}')

    # get code, source, destination, recentage from arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-w', '--width', type= int, help='Enter the new width value, height will change accordingly')
    parser.add_argument('-s', '--src', type= str, help='Enter the absolute path of input folder')
    parser.add_argument('-d', '--dest', type= str, help='Enter the absolute path of output folder')

    args = parser.parse_args()

    if args.src is not None and args.width is not None:
        resize_by_width(new_width = args.width, source = args.src, destination = args.dest)
    else:
        print('Invalid arguments passed, please check help')

else:
    print(f'Loading resize_by_image_width.py: __name__ = {__name__}')

# resize_by_percentage.py

import os
from PIL import Image
import argparse

# TODO: 3.1 resize by user determined percentage (say 50% for height and width) (proportional) res_p
def resize_by_percent_factor(resize_percent, source, destination=''):
    """
    Resize all images in given folder by user defined percentage factor
    usage: resize_by_percentage.py  [-p --prcn] [-s --src] [-d --dest] [-h --help]
    # Inputs:
        resize_percent : percentage by which images will be resized
        source : path to the folder containing images
        destination : path to the folder to place resize images

    # Functionality :
        Takes all images in the given source and resize them
        for example if image is of size 100 X 100 and resize percent is
        110, then all images will be resized to 110 X 110
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

    if not os.path.isdir(destination): # destination has to be folder
        raise ValueError(f"Destination {destination} in not a valid folder path")

    if not isinstance(resize_percent, int):
        raise ValueError(f"Invalid Source {resize_percent}")

    if resize_percent <= 0:
        raise ValueError(f"Resize percent value should be greater than 0")

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
            w, h = img.size
            w_new,h_new = int(w*resize_percent/100),int(h*resize_percent/100)
            if resize_percent <= 100: # Downsample
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
            print(f"Can't resize image")
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
    print(f'Loading from command line resize_by_percentage.py: __name__ = {__name__}')

    # get code, source, destination, recentage from arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-p', '--prcn', type= int, help='Enter the resize percentage value')
    parser.add_argument('-s', '--src', type= str, help='Enter the absolute path of input folder')
    parser.add_argument('-d', '--dest', type= str, help='Enter the absolute path of output folder')

    args = parser.parse_args()

    if args.src is not None and args.prcn is not None:
        resize_by_percent_factor(resize_percent = args.prcn, source = args.src, destination = args.dest)
    else:
        print('Invalid arguments passed, please check help')

else:
    print(f'Loading resize_by_percentage.py: __name__ = {__name__}')

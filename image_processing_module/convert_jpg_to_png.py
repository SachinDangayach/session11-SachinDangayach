# convert_jpg_to_png.py

import os
from PIL import Image
import argparse

# TODO: 1.1 jpg/jpeg to png conversion (use PIL library) j2p
def jpg_to_png(source, destination=''):
    """
    Takes folder/file path for .jpg or .jpeg images and converts it to .png.
    usage: convert_jpg_to_png.py [-s --src --source] [-d --dest] [-h --help]
    # Inputs:
        source : path to the folder/file containing images/image
        destination : path to the folder to place converted images. If null,
        destination is equals source.
    # Functionality :
        Takes all images in the given folder path and converts only those image
        which are of .jpeg or .jpg format to .png format
    """
    # Validations
    if source == None or source == '':
        raise ValueError(f"Invalid Source")

    if not isinstance(source, str):
        raise ValueError(f"Invalid Source {source}")

    if not (os.path.isfile(source) or os.path.isdir(source)):
        raise ValueError(f"Source {source} has to be file or a folder path")

    if (destination == '' or destination == None) and os.path.isdir(source): # source and destination are same folders
        destination = source
    elif (destination == '' or destination == None) and os.path.isfile(source):
        destination = source.rsplit("\\",1)[0]

    if not os.path.isdir(destination):
        raise ValueError(f"Destination {destination} in not a folder path")

    converted_files = []
    failed_files = []
    filenames = []
    target = '.png'

    if os.path.isfile(source):
        source, file_name = source.rsplit("\\",1)
        filenames.append(file_name)
    elif os.path.isdir(source):
        filenames = os.listdir(source)

    for fl in filenames:
        image_name, extension = os.path.splitext(fl)
        if extension.lower() not in {'.jpeg','.jpg'}: # Check for image files in folder
            print(f"Can't convert image {fl} to {image_name+target}")
            failed_files.append(fl)
            continue

        try:
            im = Image.open(os.path.join(source, fl))
            new_img_fl = image_name+target
            im.save(os.path.join(destination, new_img_fl))
            im.close()
            if source == destination:
                os.remove(os.path.join(source, fl))
            converted_files.append(fl)
            print(f'Image {fl} converted to  {image_name+target}')
        except OSError:
            print(f"Can't convert image {fl} to {image_name+target}")
        # For permission related errors
        except PermissionError:
            print("Operation not permitted.")
    if len(failed_files) == len(filenames):
        print(f'no files to convert')
        return True
    elif len(converted_files) > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(f'Loading from command line convert_jpg_to_png.py: __name__ = {__name__}')

    # get code, source, destination from arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-s', '--src', type= str, help='Enter the absolute path of input file/folder')
    parser.add_argument('-d', '--dest', type= str, help='Enter the absolute path of output folder')

    args = parser.parse_args()

    if args.src is not None:
        jpg_to_png(source = args.src, destination = args.dest)
    else:
        print('Invalid arguments passed, please check help')

else:
    print(f'Loading convert_jpg_to_png.py: __name__ = {__name__}')

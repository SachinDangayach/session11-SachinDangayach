"""Assignment for session 11 for Py Module mean_current_location"""
import os
from PIL import Image

# TODO: 1.1 jpg/jpeg to png conversion (use PIL library) j2p
def jpg_to_png(folder_path):
    """Takes path for folder with .jpg or .jpeg image and converts it to .png"""

    filenames = os.listdir(folder_path)
    target = '.png'
    for fl in filenames:
        image_name, extension = os.path.splitext(fl)
        if extension not in {'.jpeg','.jpg'}: # Check for image files in folder
            continue

        try:
            im = Image.open(os.path.join(folder_path, fl))
            new_img_fl = image_name+target
            im.save(os.path.join(folder_path, new_img_fl))
            im.close()
            os.remove(os.path.join(folder_path, fl))
            print(f'Image {image_name} converted to  {target}')
        except OSError:
            print(f'Cannot convert image {image_name} to {target}')


# TODO: 1.2 png to jpg conversion (use PIL library) p2j
def png_to_jpg(folder_path):
    """Takes path for folder with .png image and converts it to .jpg"""

    filenames = os.listdir(folder_path)
    target = '.jpg'
    for fl in filenames:
        image_name, extension = os.path.splitext(fl)
        if extension != '.png': # Check for image files in folder
            continue

        try:
            im = Image.open(os.path.join(folder_path, fl))
            new_img_fl = image_name+target
            im.save(os.path.join(folder_path, new_img_fl))
            im.close()
            os.remove(os.path.join(folder_path, fl))
            print(f'Image {image_name} converted to  {target}')
        except OSError:
            print(f'Cannot convert image {image_name} to {target}')

# TODO: 1.3.1 resize by user determined percentage (say 50% for height and width) (proportional) res_p
def resize_by_percent_factor(folder_path,resize_percent):
    """
    Resize all images in given folder by user
    defined percentage factor
    """
    filenames = os.listdir(folder_path)

    for fl in filenames:
        file, extension = os.path.splitext(fl)
        if extension not in {'.png','.jpeg','.jpg'}: # Check for image files in folder
            continue
        img = Image.open(os.path.join(folder_path, fl))
        w, h = img.size
        w_new,h_new = int(w*resize_percent/100),int(h*resize_percent/100)
        if resize_percent <= 100: # Downsample
            img = img.resize((w_new,h_new),Image.ANTIALIAS)
            img.save(os.path.join(folder_path, fl))
            img.close()
            print(fl, w_new,h_new)
        else: # Upsample
            img = img.resize((w_new,h_new),Image.BILINEAR)
            img.save(os.path.join(folder_path, fl))
            img.close()
            print(fl, w_new,h_new)

# TODO: 1.3.2 resize by user determined width (proportional) res_w
def resize_by_width(folder_path,new_width):
    """
    Resize all images in proportion in a given folder by user
    defined width
    """
    filenames = os.listdir(folder_path)

    for fl in filenames:
        file, extension = os.path.splitext(fl)
        if extension not in {'.png','.jpeg','.jpg'}: # Check for image files in folder
            continue
        img = Image.open(os.path.join(folder_path, fl))
        w, h = img.size # Get size of image
        resize_factor = new_width/w # Calculate resizing factor
        w_new,h_new = int(new_width),int(h*resize_factor)
        if resize_factor < 1: # Downsample
            img = img.resize((w_new,h_new),Image.ANTIALIAS)
            img.save(os.path.join(folder_path, fl))
            img.close()
            print(fl, w_new,h_new)
        else: # Upsample
            print(fl, w_new,h_new)
            img = img.resize((w_new,h_new),Image.BILINEAR)
            img.save(os.path.join(folder_path, fl))
            img.close()
            print(fl, w_new,h_new)

# TODO: 1.3.3 resize by user determined height (proportional) res_h
def resize_by_height(folder_path,new_height):
    """
    Resize all images in proportion in a given folder by user
    defined height
    """
    filenames = os.listdir(folder_path)

    for fl in filenames:
        file, extension = os.path.splitext(fl)
        if extension not in {'.png','.jpeg','.jpg'}: # Check for image files in folder
            continue
        img = Image.open(os.path.join(folder_path, fl))
        w, h = img.size # Get size of image
        resize_factor = new_height/w # Calculate resizing factor
        w_new,h_new = int(w*resize_factor),new_height
        if resize_factor < 1: # Downsample
            print(fl, w_new,h_new)
            img = img.resize((w_new,h_new),Image.ANTIALIAS)
            img.save(os.path.join(folder_path, fl))
            img.close()
            print(fl, w_new,h_new)
        else: # Upsample
            print(fl, w_new,h_new)
            img = img.resize((w_new,h_new),Image.BILINEAR)
            img.save(os.path.join(folder_path, fl))
            img.close()
            print(fl, w_new,h_new)

# TODO: 1.4.1 center square/rectangle crop by user-determined pixels crp_px
def crop_by_pixels(folder_path, w_pixel, h_pixel):
    """
    crop the image by given pixels
    """
    filenames = os.listdir(folder_path)

    for fl in filenames:
        file, extension = os.path.splitext(fl)
        if extension not in {'.png','.jpeg','.jpg'}: # Check for image files in folder
            continue
        img = Image.open(os.path.join(folder_path, fl))
        w, h = img.size # Get size of image
        if w < w_pixel or h < h_pixel:
            print(f"Image {fl} size is less than crop size, can't be cropped")
            img.close()
            continue

        # Setting the points for cropped image
        left = int(w/2 - w_pixel/2)
        top =  int(h/2 - h_pixel/2)
        right = int(left + w_pixel)
        bottom = int(top + h_pixel)

        # Cropped image of above dimension
        # (It will not change orginal image)
        img = img.crop((left, top, right, bottom))

        img.save(os.path.join(folder_path, fl))
        img.close()
        print(f'Image {fl} cropped successfully')

# TODO: 1.4.2 centre square/rectangle crop by user-determined percentage (crop to 50%/70%) crp_p
def crop_by_percent(folder_path, w_percent, h_percent):
    """
    crop the image by given pixels
    """
    filenames = os.listdir(folder_path)

    for fl in filenames:
        file, extension = os.path.splitext(fl)
        if extension not in {'.png','.jpeg','.jpg'}: # Check for image files in folder
            continue
        img = Image.open(os.path.join(folder_path, fl))
        w, h = img.size # Get size of image
        if w_percent > 100 or h_percent >100:
            print(f"Image {fl} can't be cropped more than 100% of its size")
            img.close()
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

        img.save(os.path.join(folder_path, fl))
        img.close()
        print(f'Image {fl} cropped successfully')

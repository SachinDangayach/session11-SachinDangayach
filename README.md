
# EPAI Session 11 Assignment by Sachin Dangayach

This assignment is based on the concepts of "Modules".  We have created seven python files with specific functionality as per the given assignment to convert images from jpg/ jpeg to png, resize these images by width, height or percentage factors, crop these images by pixel values or percentage of width and height. All of these can be called from command line by passing required arguments. We have created \_\_main__.py which helps to call all of the modules from command line. This helps also to create a model by placing all of these files in a folder named image_processing_module. We have also created an application named app.zip by zipping the individual code files.

# Below are key functions, Modules and applications in the Repo.

### 1.  jpg_to_png : jpg/jpeg to png conversion (use PIL library)  ( j2p is arg from main)
Module convert_jpg_to_png
    Takes folder/file path for .jpg or .jpeg images and converts it to .png.
    usage: convert_jpg_to_png.py [-s --src --source] [-d --dest] [-h --help]
    # Inputs:
        source : path to the folder/file containing images/image
        destination : path to the folder to place converted images. If null,
        destination is equals source.
    # Functionality :
        Takes all images in the given folder path and converts only those image
        which are of .jpeg or .jpg format to .png format
### 2 . png_to_jpg :  png to jpg conversion (use PIL library) ( p2j is arg from main)
Module convert_png_to_jpg
    Takes folder/file path for .png images and converts it to .jpg.
    usage: convert_png_to_jpg.py [-s --src] [-d --dest] [-h --help]
    # Inputs:
        source : path to the folder/file containing images/image
        destination : path to the folder to place converted images. If null,
        destination is equals source.
    # Functionality :
        Takes all images in the given folder path and converts only those image
        which are of .png format to .jpg format

### 3. crop_by_percent : centre square/rectangle crop by user-determined percentage (crop to 50%/70%) ( crp_p is arg from main)
Module resize_by_percentage
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

### 4. crop_by_pixels : center square/rectangle crop by user-determined pixels ( crp_px is arg from main)
Module crop_by_pixels_value
    crop the image by given pixels
    usage: crop_by_pixels_value.py [-w --wdth] [-h --hgth] [-s --src] [-d --dest] [-h --help]

    # Inputs:
        w_pixel : pixel value by which images width will be cropped
        h_pixel :  pixel value by which images height will be cropped
        source : path to the folder containing images
        destination : path to the folder to place resize images

    # Functionality :
        Takes all images in the given source and crop as per given pixel
        values of width and height
        for example, the image is of size 100 X 100 and pixel values are w_pixel = 10
        and h_pixel = 20, new size of the image will be 90 X 80 cropped from center

### 5. resize_by_height :  resize by user determined height (proportional) ( res_h is arg from main)
Module resize_by_image_height
	Return the oldest person's age of fake profiles stored in named tuple of named tuple
    Resize all images in proportion in a given folder by user
    defined height
    usage: resize_by_height.py [-h --hgth] [-s --src] [-d --dest] [-h --help]

    # Inputs:
        new_height : new height to which images will be resized.
                    width will be adjusted in proportion
        source : path to the folder containing images
        destination : path to the folder to place resize images

    # Functionality :
        Takes all images in the given folder path and resize as per give height
        for example if image is of size 100 X 100 and new height is 120, then
        the new width to maintain the proportion will be 120, then all images
        will be resized to 120 X 120

### 6. resize_by_width : resize by user determined width (proportional)  ( res_w is arg from main )
Module crop_by_percent_value
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

### 7. resize_by_percent_factor : resize by user determined percentage (say 50% for height and width) (proportional) ( res_p is arg from main )
Module crop_by_pixels_value
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

### 8. \_\_main__ : module that exposes all these features (using argparse)
We use argparse to call various modules from command line by passing arguments.

### 9. Module image_processing_module: Its a module for image processing functions
Once we place \_\_main__.py in the folder image_processing_module, it becomes a module. It contains convert_jpg_to_png','convert_png_to_jpg', 'resize_by_percentage',   'resize_by_image_width', 'resize_by_image_height', 'crop_by_percent_value', 'crop_by_pixels_value'

### 10. app.zip : Created a zipped app, that exposes all of these features from command line. We create an application by create application by following command-
python -m zipfile -c app.zip \_\_main__.py convert_jpg_to_png.py convert_png_to_jpg.py resize_by_percentage.py resize_by_image_width.py resize_by_image_height.py crop_by_percent_value.py crop_by_pixels_value.py

# Below are test cases functions in test_session11.py file.

## Check for coding standards-

## 1. test_readme_exists :
Test for readme exists

## 2. test_readme_contents :
Test for readme contents are more than 500 words

## 3. test_readme_proper_description :
Test for all important functions/class described well in your README.md file

## 4. test_readme_file_for_formatting :
Test for readme formatting

## 5. test_indentations :
Test for source code formatting. No tabs but four spaces are used for indentation

## 6. test_function_name_had_cap_letters :
Test for no function is with capitals in source code

## 7. test_function_count :
Test to check minimum 20 functions are provided

## 8. test_function_repeatations:
Test for no function is repeated

## 9. test_doc_string:
Test to check doc strings

## 10. test_function_name_had_cap_letters :
Test for no function is with capitals in source code

# Test cases for assignments

## 11. test_ip_module:
Test to check the image processing module is working

## 12. test_ip_app:
Test to check the app.zip for image processing module is working

## 13. test_jpg_to_png:
Test convert_jpg_to_png.py module

## 14. test_png_to_jpg:
Test convert_png_to_jpg.py module

## 15. test_resize_by_percent_factor:
Test resize_by_percentage.py module

## 16. test_resize_by_width:
Test resize_by_image_width.py module

## 17. test_resize_by_height:
Test resize_by_image_height.py module

## 18. test_crop_by_percent:
Test crop_by_percent_value.py module

## 19. test_crop_by_pixels:
Test crop_by_pixels_value.py module

## 20. test_jpg_to_png_image:
Test convert_jpg_to_png.py module for single image

## 21. test_png_to_jpg_image:
Test convert_png_to_jpg.py module for single image

## 22. test_jpg_to_png_to_dest:
Test convert_jpg_to_png to destination module

## 23. test_png_to_jpg_to_dest:
Test convert_png_to_jpg to destination module

## 24. test_resize_by_percent_factor_to_dest:
Test resize_by_percentage to destination module

## 25. test_resize_by_width_to_dest:
Test resize_by_image_width to destination module

## 26. test_resize_by_height_to_dest:
Test resize_by_image_height module to destination module

## 27. test_crop_by_percent_to_dest:
Test crop_by_percent_value to destination module

## 28. test_crop_by_pixels_to_dest:
Test crop_by_pixels_value to destination module

## 29. test_jpg_to_png_image_to_dest:
Test convert_jpg_to_png for single images to destination module

## 30. test_png_to_jpg_image_to_dest:
Test convert_png_to_jpg for single images to destination module

## 31. test_value_errors:
Test value errors in function call

## 32. test_type_errors:
Test Type errors in function call

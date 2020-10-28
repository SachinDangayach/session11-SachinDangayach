import pytest
import re
import inspect
import os
import shutil
import sys
import test_session11
from image_processing_module import convert_jpg_to_png
from image_processing_module import convert_png_to_jpg
from image_processing_module import resize_by_percentage
from image_processing_module import resize_by_image_width
from image_processing_module import resize_by_image_height
from image_processing_module import crop_by_percent_value
from image_processing_module import crop_by_pixels_value

ip_modules = ['convert_jpg_to_png','convert_png_to_jpg', 'resize_by_percentage',
              'resize_by_image_width','resize_by_image_height', 'crop_by_percent_value',
              'crop_by_pixels_value']

README_CONTENT_CHECK_FOR = [
    'j2p', 'p2j', 'res_w', 'res_h', 'res_p', 'crp_p', 'crp_px',
    'image_processing_module', 'convert_jpg_to_png',
    'convert_png_to_jpg', 'resize_by_percentage', 'resize_by_image_width',
    'resize_by_image_height', 'crop_by_percent_value', 'crop_by_pixels_value'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    """get file content"""
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    """Check readme description"""
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    """Check readme formatting"""
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically
    significant indenting.'''
    if not ip_modules:
        for module in ip_modules:
            lines = inspect.getsource(module)
            spaces = re.findall('\n +.', lines)
            for space in spaces:
                assert len(space) % 4 == 2, f"Your script contains misplaced indentations"
                assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    """Check no capital letters are used in function names"""
    for module in ip_modules:
        functions = inspect.getmembers(module, inspect.isfunction)
        for function in functions:
            assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_count():
    """Check function count"""
    functions = inspect.getmembers(test_session11, inspect.isfunction)
    assert len(functions) > 0, 'Minimum 20 testcase required'

def test_function_repeatations():
    '''to check repeating fucntions'''
    functions = inspect.getmembers(test_session11, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Duplicate testcase found'

def test_doc_string():
    """Check for doc strings"""
    assert bool(convert_jpg_to_png.jpg_to_png.__doc__), "No DocString for JPG to PNG converter"
    assert bool(convert_png_to_jpg.png_to_jpg.__doc__), "No DocString for PNG to JPG converter"
    assert bool(resize_by_percentage.resize_by_percent_factor.__doc__), "No DocString for resize by percentage factor"
    assert bool(resize_by_image_width.resize_by_width.__doc__), "No DocString for resize by width"
    assert bool(resize_by_image_height.resize_by_height.__doc__), "No DocString for resize by height"
    assert bool(crop_by_percent_value.crop_by_percent.__doc__), "No DocString for crop by pixel"
    assert bool(crop_by_pixels_value.crop_by_pixels.__doc__), "No DocString for crop by percent"

############################## Modules Validations #############################

# TODO: 1 Test image_processing_module module
def test_ip_module():
    """
    Test to check the image processing module is working
    """

    run_code = 'python image_processing_module j2p -s "Images"'
    execute_command = os.system(run_code)
    assert not execute_command, "JPG to PNG Conversion failed"

    run_code = 'python image_processing_module p2j -s "Images"'
    execute_command = os.system(run_code)
    assert not execute_command, "PNG to JPG Conversion failed"

    run_code = 'python image_processing_module res_p -s "Images" -p 80'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Resize by Percent failed"

    run_code = 'python image_processing_module res_w -s "Images" -w 800'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Resize by Width failed"

    run_code = 'python image_processing_module res_h -s "Images" -ht 800'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Resize by Height failed"

    run_code = run_code = 'python image_processing_module crp_p -s "Images" -w 10 -ht 20'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Cropping by Percent failed"

    run_code = 'python image_processing_module crp_px -s "Images" -w 10 -ht 5'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Cropping by Pixel failed"

# TODO: 2 Test app for image processing
def test_ip_app():
    """
    Test to check the app.zip for image processing module is working
    """

    run_code = 'python app.zip j2p -s "Images"'
    execute_command = os.system(run_code)
    assert not execute_command, "JPG to PNG Conversion failed"

    run_code = 'python app.zip p2j -s "Images"'
    execute_command = os.system(run_code)
    assert not execute_command, "PNG to JPG Conversion failed"

    run_code = 'python app.zip res_p -s "Images" -p 150'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Resize by Percent failed"

    run_code = 'python app.zip res_w -s "Images" -w 800'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Resize by Width failed"

    run_code = 'python app.zip res_h -s "Images" -ht 2000'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Resize by Height failed"

    run_code = run_code = 'python app.zip crp_p -s "Images" -w 5 -ht 10'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Cropping by Percent failed"

    run_code = 'python app.zip crp_px -s "Images" -w 10 -ht 2'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Cropping by Pixel  failed"

# TODO: 3 Test convert_jpg_to_png.py module
def test_jpg_to_png():
    """Test convert_jpg_to_png.py module """

    run_code = 'python ./image_processing_module/convert_jpg_to_png.py -s "Images"'
    execute_command = os.system(run_code)
    assert not execute_command, "Conversion to PNG by convert_jpg_to_png.py failed"

# TODO: 4 Test convert_png_to_jpg.py module
def test_png_to_jpg():
    """Test convert_png_to_jpg.py module"""

    run_code = 'python ./image_processing_module/convert_png_to_jpg.py -s "Images"'
    execute_command = os.system(run_code)
    assert not execute_command, "Conversion to JPEG by convert_png_to_jpg.py failed"


# TODO: 5 Test resize_by_percentage.py module
def test_resize_by_percent_factor():
    """Test resize_by_percentage.py module"""

    run_code = 'python ./image_processing_module/resize_by_percentage.py -s "Images" -p 150'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Resize by Percent failed"


# TODO: 6 Test resize_by_image_width.py module
def test_resize_by_width():
    """Test resize_by_image_width.py module"""

    run_code = 'python ./image_processing_module/resize_by_image_width.py -s "Images" -w 800'
    execute_command = os.system(run_code)
    assert not execute_command, "Image resize by Width using  resize_by_image_width.py failed"

# TODO: 7 Test resize_by_image_height.py module
def test_resize_by_height():
    """Test resize_by_image_height.py module"""

    run_code = 'python ./image_processing_module/resize_by_image_height.py -s "Images" -ht 800'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Resize by Height using resize_by_image_height.py failed"

# TODO: 8 Test crop_by_percent_value.py module
def test_crop_by_percent():
    """Test crop_by_percent_value.py module"""

    run_code = 'python ./image_processing_module/crop_by_pixels_value.py -s "Images" -w 10 -ht 20'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Cropping by Percent using crop_by_pixels_value.py failed"

# TODO: 9 Test crop_by_pixels_value module
def test_crop_by_pixels():
    """Test crop_by_pixels_value.py module"""

    run_code = run_code = 'python ./image_processing_module/crop_by_percent_value.py -s "Images" -w 20 -ht 30'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Cropping by Pixel using crop_by_percent_value.py failed"

# TODO: 10 Test convert_jpg_to_png.py module for single image
def test_jpg_to_png_image():
    """Test convert_jpg_to_png.py module for single image"""

    run_code = 'python ./image_processing_module/convert_jpg_to_png.py -s "Images/img_002.jpg"'
    execute_command = os.system(run_code)
    assert not execute_command, "Conversion to PNG by convert_jpg_to_png.py failed"

# TODO: 11 Test convert_png_to_jpg.py module for single image
def test_png_to_jpg_image():
    """Test convert_png_to_jpg.py module for single image"""

    run_code = 'python ./image_processing_module/convert_png_to_jpg.py -s "Images/img_002.png"'
    execute_command = os.system(run_code)
    assert not execute_command, "Conversion to JPEG by convert_png_to_jpg.py failed"

# TODO: 12 Test convert_jpg_to_png to destination module
def test_jpg_to_png_to_dest():
    """Test convert_jpg_to_png to destination module"""
    # # Reset image folder
    # reset_folder("Images", "Dest", "Images_Master")

    run_code = 'python ./image_processing_module/convert_jpg_to_png.py -s "Images" -d "Dest"'
    execute_command = os.system(run_code)
    assert not execute_command, "Conversion to PNG by convert_jpg_to_png.py failed"

# TODO: 13 Test convert_png_to_jpg to destination module
def test_png_to_jpg_to_dest():
    """Test convert_png_to_jpg to destination module"""

    run_code = 'python ./image_processing_module/convert_png_to_jpg.py -s "Images" -d "Dest"'
    execute_command = os.system(run_code)
    assert not execute_command, "Conversion to JPEG by convert_png_to_jpg.py failed"

# TODO: 14 Test resize_by_percentage to destination module
def test_resize_by_percent_factor_to_dest():
    """Test resize_by_percentage to destination module"""

    run_code = 'python ./image_processing_module/resize_by_percentage.py -s "Images" -d "Dest"  -p 150'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Resize by Percent failed"

# TODO: 15 Test resize_by_image_width to destination module
def test_resize_by_width_to_dest():
    """Test resize_by_image_width to destination module"""

    run_code = 'python ./image_processing_module/resize_by_image_width.py -s "Images" -d "Dest" -w 800'
    execute_command = os.system(run_code)
    assert not execute_command, "Image resize by Width using  resize_by_image_width.py failed"

# TODO: 16 Test resize_by_image_height module to destination module
def test_resize_by_height_to_dest():
    """Test resize_by_image_height module to destination module"""

    run_code = 'python ./image_processing_module/resize_by_image_height.py -s "Images" -d "Dest" -ht 800'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Resize by Height using resize_by_image_height.py failed"

# TODO: 17 Test crop_by_percent_value to destination module
def test_crop_by_percent_to_dest():
    """Test crop_by_percent_value to destination module"""

    run_code = 'python ./image_processing_module/crop_by_percent_value.py -s "Images" -d "Dest" -w 10 -ht 20'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Cropping by Percent using crop_by_percent_value.py failed"

# TODO: 18 Test crop_by_pixels_value to destination module
def test_crop_by_pixels_to_dest():
    """Test crop_by_pixels_value to destination module"""

    run_code = run_code = 'python ./image_processing_module/crop_by_pixels_value.py -s "Images" -d "Dest" -w 10 -ht 5'
    execute_command = os.system(run_code)
    assert not execute_command, "Image Cropping by Pixel using crop_by_percent_value.py failed"

# TODO: 19 Test convert_jpg_to_png for single images to destination module
def test_jpg_to_png_image_to_dest():
    """Test convert_jpg_to_png for single images to destination module"""

    run_code = 'python ./image_processing_module/convert_jpg_to_png.py -s "Images/img_002.jpg" -d "Dest"'
    execute_command = os.system(run_code)
    assert not execute_command, "Conversion to PNG by convert_jpg_to_png.py failed"

# TODO: 20 Test convert_png_to_jpg for single images to destination module
def test_png_to_jpg_image_to_dest():
    """Test convert_png_to_jpg for single images to destination module"""

    run_code = 'python ./image_processing_module/convert_png_to_jpg.py -s "Images/img_002.png" -d "Dest"'
    execute_command = os.system(run_code)
    assert not execute_command, "Conversion to JPEG by convert_png_to_jpg.py failed"

# TODO: 21 Test value errors in functon calls
def test_value_errors():
    """Test value errors in function call"""
    # Reset image folder
    # reset_folder("Images", "Dest", "Images_Master")

    with pytest.raises(ValueError):
        convert_jpg_to_png.jpg_to_png(source = "./abc")
    with pytest.raises(ValueError):
        convert_png_to_jpg.png_to_jpg(source = "./abc")
    with pytest.raises(ValueError):
        resize_by_percentage.resize_by_percent_factor(resize_percent =-10 , source = "Images")
    with pytest.raises(ValueError):
        resize_by_image_width.resize_by_width(new_width = -10, source = "Images")
    with pytest.raises(ValueError):
        resize_by_image_height.resize_by_height(new_height = -19, source = "Images")
    with pytest.raises(ValueError):
        crop_by_percent_value.crop_by_percent(w_percent = -200, h_percent = 20, source = "Images")
    with pytest.raises(ValueError):
        crop_by_percent_value.crop_by_percent(w_percent = 10, h_percent = -2, source = "Images")
    with pytest.raises(ValueError):
        crop_by_percent_value.crop_by_percent(w_percent = 10, h_percent = 200, source = "Images")
    with pytest.raises(ValueError):
        crop_by_percent_value.crop_by_percent(w_percent = 120, h_percent = 2, source = "Images")
    with pytest.raises(ValueError):
        crop_by_pixels_value.crop_by_pixels(w_pixel = -10, h_pixel = 100, source = "Images")
    with pytest.raises(ValueError):
        crop_by_pixels_value.crop_by_pixels(w_pixel = 100, h_pixel = -10, source = "Images")

# TODO: 22 Test Type errors in function call
def test_type_errors():
    """Test Type errors in function call"""
    # Reset image folder
    # reset_folder("Images", "Dest", "Images_Master")

    with pytest.raises(TypeError):
        convert_jpg_to_png.jpg_to_png(source = 12)
    with pytest.raises(TypeError):
        convert_png_to_jpg.png_to_jpg(source = 797)
    with pytest.raises(TypeError):
        resize_by_percentage.resize_by_percent_factor(resize_percent = 'abc', source = "Images")
    with pytest.raises(TypeError):
        resize_by_image_width.resize_by_width(new_width = '223', source = "Images")
    with pytest.raises(TypeError):
        resize_by_image_height.resize_by_height(new_height = '00', source = "Images")
    with pytest.raises(TypeError):
        crop_by_percent_value.crop_by_percent(w_percent = '200', h_percent = 20, source = "Images")
    with pytest.raises(TypeError):
        crop_by_percent_value.crop_by_percent(w_percent = '200', h_percent = 2, source = "Images")
    with pytest.raises(TypeError):
        crop_by_pixels_value.crop_by_pixels(w_pixel = 'abc', h_pixel = 100, source = "Images")
    with pytest.raises(TypeError):
        crop_by_pixels_value.crop_by_pixels(w_pixel = 100, h_pixel = '100', source = "Images")

def reset_folder(source, oput, master):
    """Reset folders to initial state"""
    filenames = os.listdir(source)
    for fl in filenames:
        try:
            os.unlink(os.path.join(source, fl))
        except OSError:
            print('folder not deleted')

    filenames = os.listdir(oput)
    if filenames:
        for fl in filenames:
            if fl == 'dummy.txt':
                continue
            try:
                os.unlink(os.path.join(oput, fl))
            except OSError:
                print('folder not deleted')

    filenames_new = os.listdir(master)
    for fl in filenames_new:
        try:
            shutil.copy(os.path.join(master, fl), os.path.join(source, fl))
        except OSError:
            print('files not moved')

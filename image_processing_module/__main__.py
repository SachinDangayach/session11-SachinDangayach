# __main__.py

import sys
import argparse
import convert_jpg_to_png
import convert_png_to_jpg
import resize_by_percentage
import resize_by_image_width
import resize_by_image_height
import crop_by_percent_value
import crop_by_pixels_value

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=__doc__)
    parent_parser = argparse.ArgumentParser(add_help=False)

    parent_parser.add_argument('-s', '--src', type= str, help='Enter the absolute path of input file/folder')
    parent_parser.add_argument('-d', '--dest', type= str, help='Enter the absolute path of output folder')

    subparsers = parser.add_subparsers(help='Image Processing Options')

    j2p_parser = subparsers.add_parser('j2p', parents = [parent_parser],help='JPG/JPEG to PNG Converter')
    p2j_parser = subparsers.add_parser('p2j', parents = [parent_parser],help='PNG to JPG Converter')

    res_p_parser = subparsers.add_parser('res_p', parents = [parent_parser],help='Resize Image by percent')
    res_p_parser.add_argument('-p', '--prcn', type= int, help='Enter the resize percentage value')

    res_w_parser = subparsers.add_parser('res_w', parents = [parent_parser],help='Resize Image in proportion to width')
    res_w_parser.add_argument('-w', '--width', type= int, help='Enter the new width value, height will change accordingly')

    res_h_parser = subparsers.add_parser('res_h', parents = [parent_parser], help='Resize Image in proportion to height')
    res_h_parser.add_argument('-ht', '--height', type= int, help='Enter the new height value, width will change accordingly')

    crp_px_parser = subparsers.add_parser('crp_px', parents = [parent_parser], help='Crop the image by given pixels values')
    crp_px_parser.add_argument('-w', '--width', type= int, help='Enter the value of width to be center cropped')
    crp_px_parser.add_argument('-ht', '--height', type= int, help='Enter the value of height to be center cropped')

    crp_p_parser = subparsers.add_parser('crp_p', parents = [parent_parser], help='Crop the image by given pixels precentage')
    crp_p_parser.add_argument('-w', '--width', type= int, help='Enter the % value of width to be center cropped')
    crp_p_parser.add_argument('-ht', '--height', type= int, help='Enter the % value of height to be center cropped')


    args = parser.parse_args()

    if(len(sys.argv) == 1):
        print("Check help for available Image Processing options")
    elif(len(sys.argv) == 2):
        print("Check help for selected operation arguments")
    else:
        if(sys.argv[1] == 'j2p'):
            convert_jpg_to_png.jpg_to_png(source = args.src, destination = args.dest)
        elif(sys.argv[1] == 'p2j'):
            convert_png_to_jpg.png_to_jpg(source = args.src, destination = args.dest)
        elif(sys.argv[1] == 'res_p'):
            resize_by_percentage.resize_by_percent_factor(resize_percent = args.prcn, source = args.src, destination = args.dest)
        elif(sys.argv[1] == 'res_w'):
            resize_by_image_width.resize_by_width(new_width = args.width, source = args.src, destination = args.dest)
        elif(sys.argv[1] == 'res_h'):
            resize_by_image_height.resize_by_height(new_height = args.height, source = args.src, destination = args.dest)
        elif(sys.argv[1] == 'crp_px'):
            crop_by_percent_value.crop_by_percent(w_percent = args.width, h_percent = args.height, source = args.src, destination = args.dest)
        elif(sys.argv[1] == 'crp_p'):
            crop_by_pixels_value.crop_by_pixels(w_pixel = args.width, h_pixel = args.height, source = args.src, destination = args.dest)

# import argparse

# parser = argparse.ArgumentParser(
#                     prog='Turtle Encoder 1.0.0 🐢',
#                     description='Takes text, encodes as binary, represents 1s and 0 as turtles.',
#                     epilog='Save the turtles, keep the environment clean')
# parser.add_argument('phrase', type=ascii, nargs='?', default='hello world!', help='This is a phrase contained within quotes.')

# args = parser.parse_args()
# args.phrase = args.phrase[1:-1] # gets rid of quotes

import os
from PIL import Image

folder_path = "images/"
contents = os.listdir(folder_path)

output_folder = "out"
os.makedirs(output_folder, exist_ok=True)

width, height = 10,8
resolution = 300
art_canvas = Image.new(mode:='RGB', size=[width*resolution, height*resolution], color='white')
x = 0
y = 0
columns = 1 # could be 3, 1, 4?
grid_columns = columns * 10 # height the same, as we're dealing with square ratio images.
grid_width = int(width * resolution / grid_columns)

#rows: Determine from length of binary message (i.e. list has 4 items, each of an 8 digit number)
    # factor in number columns -- or grid columns! -- 
    # for a 2 column image, new row every 16 turtle images. modulus % 8*columns
    
# do math, something like the modulo function to see where you are. i.e. remainder 1 or 0 print (check) print a blank sq.

for pic in contents:
    img = Image.open(folder_path + pic)
    resized_img = img.resize((grid_width, grid_width), Image.LANCZOS) 
    if x > 400: resized_img = resized_img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    art_canvas.paste(resized_img, (x, y))
    x += grid_width # make dynamic
    
# would need a Y += int step for a new column
    
# image1 = Image.open(f"{folder_path}green_turtle.jpg")
# resized_image1 = image1.resize((200, 200))
# art_canvas.paste(resized_image1, (10,10))

file_path = os.path.join(output_folder, "turtle_image.jpg")
art_canvas.save(file_path, dpi=(resolution, resolution), quality=100)

print(f"Image saved to {file_path}")


def main():
    print("Turtle Encoder 1.0.0 🐢")
    # message = input("Enter your message: ")
    # text_to_8bit(message)
    # print(contents)
    
def text_to_charcode(message):
    return [ord(char) for char in message]

def ord_to_binary(ord_message):
    return [bin(num) for num in ord_message]
    
def eightify(bin_string):
    """Example: converts '0b1100001' to '01100001' ensuring each binary number is an 8 digit long string"""
    num = bin_string.replace("0b", "").zfill(8)
    return num

def bin_to_8bit(bin_list):
    return [eightify(bin_str) for bin_str in bin_list]

def text_to_8bit(message, debug=True):
    ord_message = text_to_charcode(message)
    binary_message = ord_to_binary(ord_message)
    eight_bit = (bin_to_8bit(binary_message))
    if debug: print(ord_message, binary_message, eight_bit, sep='\n')
    return eight_bit
    
def get_images(folder_path):
    return os.listdir(folder_path)
    
if __name__ == "__main__":
    main()
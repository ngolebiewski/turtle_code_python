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
import random
import copy

def image_queue_maker(image_list, turtle_count):
    """Shuffle in place method, rather than randomly pulling from original list, to ensure that every image is used."""
    count = 0
    turtle_queue = list()
    while count < turtle_count:
        shuffled_turtles = copy.deepcopy(image_list)
        random.shuffle(shuffled_turtles)
        turtle_queue.extend(shuffled_turtles)
        count = len(turtle_queue)
        shuffled_turtles.clear()
    turtle_queue = turtle_queue[0:turtle_count] # Cuts queued list to the number of turtle characters within the message, as the while loop can overpopulate on the last iteration.
    return turtle_queue
    
def make_turtle_image(binary_message=['01101000', '01100101', '01101100', '01101100', '01101111', '00100001'], 
                      width=10, height=8, columns=2, resolution=300):

    folder_path = "images/"
    contents = os.listdir(folder_path)
    output_folder = "out"
    os.makedirs(output_folder, exist_ok=True)

    art_canvas = Image.new(mode='RGB', size=[width*resolution, height*resolution], color='white')
    grid_columns = columns * 10 # height the same, as we're dealing with square ratio images.
    grid_width = int(width * resolution / grid_columns)
    x = 0
    y = 0
    turtle_count = len(binary_message)*8
    
    turtle_queue = image_queue_maker(contents, turtle_count) # List of image files, randomized for num chars within binary message
    
    for index, octet in enumerate(binary_message):
        if index % columns == 0:  #logic check to see if need a new row line. inits 
            y += grid_width
            #reset x when beginning a new line, like a typewriter starting a new line
            if columns == 2: 
                x = int(grid_width * .25) 
            elif columns == 3: 
                x = int(grid_width * .5)
            else: 
                x = 0 
        x += int(grid_width) # initial blank space
    
        # print 8 turtles
        for num in octet:
            img = Image.open(folder_path + turtle_queue.pop())
            resized_img = img.resize((grid_width, grid_width), Image.LANCZOS) # Hi-fi resampling so jpg not jagged.
            if num == '1': resized_img = resized_img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            art_canvas.paste(resized_img, (x, y))
            x += grid_width # shift typewriter over one space
        # final blank space
        x += int(grid_width * .5)
        
    
    #rows: Determine from length of binary message (i.e. list has 4 items, each of an 8 digit number)
        # factor in number columns -- or grid columns! -- 
        # for a 2 column image, new row every 16 turtle images. modulus % 8*columns
        
    # do math, something like the modulo function to see where you are. i.e. remainder 1 or 0 print (check) print a blank sq.

    # for pic in contents:
    #     img = Image.open(folder_path + pic)
    #     resized_img = img.resize((grid_width, grid_width), Image.LANCZOS) # Hi-fi resampling so jpg not jagged.
    #     if x > 400: resized_img = resized_img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    #     art_canvas.paste(resized_img, (x, y))
    #     x += grid_width # make dynamic
        
    # would need a Y += int step for a new column

    file_path = os.path.join(output_folder, "turtle_image.jpg")
    art_canvas.save(file_path, dpi=(resolution, resolution), quality=100)

    print(f"Image saved to {file_path}")
    
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
    
def main():
    print("Turtle Encoder 1.0.0 🐢")
    message = input("Enter your message: ")
    encoded_message = text_to_8bit(message)
    make_turtle_image(encoded_message, width=20, height=16, columns=1, resolution=72)
    
if __name__ == "__main__":
    main()
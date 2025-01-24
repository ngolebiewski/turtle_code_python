import os
from PIL import Image
import random
import copy

def main():
    """Set the paramaters on the make_turtle_image function, w&h in inches to adjust the format for the image output."""
    print(style.GREEN + "Turtle Encoder 1.0.0 🐢" + style.RESET)
    message = input("Enter your message: ")
    encoded_message = text_to_8bit(message)
    make_turtle_image(encoded_message, width=20, height=16, columns=3, resolution=72)

class style():
    GREEN = '\033[92m'
    RESET = '\033[0m'

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
    """Converts a text message to ordinal numbers to binary and returns the 8-bit binary List."""
    ord_message = text_to_charcode(message)
    binary_message = ord_to_binary(ord_message)
    eight_bit = (bin_to_8bit(binary_message))
    if debug: print(ord_message, binary_message, eight_bit, sep='\n')
    return eight_bit
    
def get_images(folder_path):
    return os.listdir(folder_path)

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
    turtle_queue = turtle_queue[0:turtle_count] # Cuts list to actual length of message, while loop can add in some extra.
    return turtle_queue
    
def make_turtle_image(binary_message=['01101000', '01100101', '01101100', '01101100', '01101111', '00100001'], 
                      width=10, height=8, columns=2, resolution=300):
    """Turns the 8-bit binary message into a turtle image and exports the jpg file"""
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
        # Check to see if we need a new line, and resets x.
        if index % columns == 0: 
            y += grid_width
            if columns == 2: 
                x = int(grid_width * .25) 
            elif columns == 3: 
                x = int(grid_width * .5)
            else: 
                x = 0 
                
        # initial blank space
        x += int(grid_width) 
    
        # print 8 turtles
        for num in octet:
            img = Image.open(folder_path + turtle_queue.pop())
            resized_img = img.resize((grid_width, grid_width), Image.LANCZOS) # Hi-fi resampling so jpg not jagged.
            if num == '1': resized_img = resized_img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            art_canvas.paste(resized_img, (x, y))
            x += grid_width # shift typewriter over one space
            
        # final blank space
        x += int(grid_width * .5)
        
    # Save the image file
    file_path = os.path.join(output_folder, "turtle_image.jpg")
    art_canvas.save(file_path, dpi=(resolution, resolution), quality=100)
    print(f"Image saved to {file_path}")
    return file_path
    
if __name__ == "__main__":
    main()
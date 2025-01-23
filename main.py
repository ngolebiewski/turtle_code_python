# import argparse

# parser = argparse.ArgumentParser(
#                     prog='Turtle Encoder 1.0.0 🐢',
#                     description='Takes text, encodes as binary, represents 1s and 0 as turtles.',
#                     epilog='Save the turtles, keep the environment clean')
# parser.add_argument('phrase', type=ascii, nargs='?', default='hello world!', help='This is a phrase contained within quotes.')

# args = parser.parse_args()
# args.phrase = args.phrase[1:-1] # gets rid of quotes

def main():
    print("Turtle Encoder 1.0.0 🐢")
    message = input("Enter your message: ")
    text_to_8bit(message)
    

def text_to_charcode(message):
    return [ord(char) for char in message]

def ord_to_binary(ord_message):
    return [bin(num) for num in ord_message]
    
def eightify(bin_string):
    """Example: converts '0b1100001' to '01100001' ensuring each binary number is an 8 digit long string"""
    num = bin_string.replace("0b", "")
    while len(num) < 8:
        num = "0" + num
    return num

def bin_to_8bit(bin_list):
    return [eightify(bin_str) for bin_str in bin_list]

def text_to_8bit(message, debug=True):
    ord_message = text_to_charcode(message)
    binary_message = ord_to_binary(ord_message)
    eight_bit = (bin_to_8bit(binary_message))
    if debug:
        print(ord_message)
        print(binary_message)
        print(eight_bit)
    return eight_bit
    
if __name__ == "__main__":
    main()
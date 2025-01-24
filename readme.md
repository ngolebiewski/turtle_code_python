# Turtle Code 🐢

## CLI Program: Encode text in binary, represent by n number of turtle images, export hi-res image for print.

## What?

- Converts a text message to ordinal numbers to binary to a list of 8-bit binary numbers. 
- Each '0' is represented by a left-facing turtle
- Each '1' is represemted by a right-facing turtle

## How to install and use.
- Clone this repo.
- Make Virtual Environment.
    a. `python3 -m venv venv`
    b. Activate: `source venv/bin/activate`
- Install necessary libraries: `pip install -r requirements.txt`
- Add left-facing turtle images into the `images` folder. 
    - Should all be SQUARE format.
- Adjust paramaters in the turtle_encoder code `make_turtle_image(encoded_message, width=20, height=16, columns=3, resolution=72)`
    - Note width and height are in inches
- Run `python3 turtle_encoder.py`

## Tech

- Python
- Pillow

## Example.

Message: "The Analytical Engine weaves algebraic patterns, just as the Jacquard loom weaves flowers and leaves" -Ada Lovelace

![lots of turtles in 3 columns](out/ada_quote.jpg)

## Todo

- Add message in plain text on lower right (?) of output image.
- Flask? --> for endpoint that a React FE can access?
- Code is a partner to this demo app: Partner to: https://turtle-encoder.onrender.com/
- Adjust row size on image output to center for less text, or adjust columns/rows for longer text Dynamically.

## Notes:

- Read up on resampling images: https://en.wikipedia.org/wiki/Lanczos_resampling
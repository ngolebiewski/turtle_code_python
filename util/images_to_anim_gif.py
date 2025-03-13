import os
import argparse
from PIL import Image

def resize_and_convert_to_gif(input_folder, output_folder="GIF_OUT", size=(400, 400), fps=8):
    """
    Resizes images in the input folder and creates an animated GIF.

    Args:
        input_folder (str): Path to the folder containing images.
        output_folder (str): Path to the folder to save the GIF. Defaults to "GIF_OUT".
        size (tuple): Target size (width, height).
        fps (int): Frames per second.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images = []
    for filename in sorted(os.listdir(input_folder)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            filepath = os.path.join(input_folder, filename)
            try:
                img = Image.open(filepath)
                img.load() #Important to load before closing.
                
                # Calculate aspect ratios
                img_width, img_height = img.size
                target_width, target_height = size

                img_ratio = img_width / img_height
                target_ratio = target_width / target_height

                if img_ratio > target_ratio:
                    # Image is wider, resize based on width
                    new_width = target_width
                    new_height = int(target_width / img_ratio)
                else:
                    # Image is taller or same aspect ratio, resize based on height
                    new_height = target_height
                    new_width = int(target_height * img_ratio)

                resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                # Create a new image with the target size and paste the resized image in the center
                final_img = Image.new('RGB', size, (255, 255, 255))  # White background
                x_offset = (target_width - new_width) // 2
                y_offset = (target_height - new_height) // 2
                final_img.paste(resized_img, (x_offset, y_offset))

                images.append(final_img)
                img.close() #Close the original image.
                resized_img.close() # Close the resized image.

            except Exception as e:
                print(f"Error processing {filename}: {e}")

    if images:
        output_gif_path = os.path.join(output_folder, 'animated.gif')
        images[0].save(output_gif_path, save_all=True, append_images=images[1:], duration=1000 // fps, loop=0, optimize=True)
        print(f"GIF created successfully: {output_gif_path}")
    else:
        print("No valid images found in the input folder.")

def main():
    parser = argparse.ArgumentParser(description="Resize images and create an animated GIF.")
    parser.add_argument("input_folder", help="Path to the input folder containing images.")
    parser.add_argument("output_folder", nargs='?', default="GIF_OUT", help="Path to the output folder for the GIF. Defaults to GIF_OUT.") #Make output_folder optional
    parser.add_argument("--size", type=str, default="400x400", help="Target size (widthxheight).")
    parser.add_argument("--fps", type=int, default=8, help="Frames per second.")

    args = parser.parse_args()

    try:
        width, height = map(int, args.size.split('x'))
        resize_and_convert_to_gif(args.input_folder, args.output_folder, size=(width, height), fps=args.fps)
    except ValueError:
        print("Invalid size format. Use widthxheight (e.g., 400x400).")

if __name__ == "__main__":
    main()
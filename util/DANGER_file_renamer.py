import os
from PIL import Image

def rename_and_truncate_jpgs(folder_path):
    """
    PURPOSE: Remove student names form the images, and delete metadata including location and original file name.
    Renames and truncates JPG files in a folder, keeping only the first two letters of the last part of the filename.
    Removes metadata.
    Logs the changes.

    Args:
        folder_path (str): The path to the folder containing the JPG files.
    """
    try:
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(".jpg"):
                filepath = os.path.join(folder_path, filename)
                try:
                    # Truncate using string slicing (faster than regex for this simple case)
                    new_filename = filename[:12] + filename[12:13] + ".jpg"

                    if new_filename != filename:  # only rename if it is a change
                        new_filepath = os.path.join(folder_path, new_filename)
                        os.rename(filepath, new_filepath)

                        # Remove metadata
                        with Image.open(new_filepath) as img:
                            data = list(img.getdata())
                            img_without_exif = Image.new(img.mode, img.size)
                            img_without_exif.putdata(data)
                            img_without_exif.save(new_filepath, "JPEG")  # Resave, removing exif.
                            img_without_exif.close()

                        print(f"Renamed and metadata removed: {filename} -> {new_filename}")

                except Exception as e:
                    print(f"Error processing {filename}: {e}")

    except FileNotFoundError:
        print(f"Error: Folder not found: {folder_path}")

def main():
    folder_path = input("Enter the folder path: ")

    # Confirm folder path and contents
    full_path = os.path.abspath(folder_path)
    print(f"This is the folder you've selected: {full_path}")

    try:
        file_list = os.listdir(folder_path)
        print("These are the contents:", ", ".join(file_list))

        confirmation = input("Do you want to proceed (Yes/no): ").lower()
        if confirmation == "yes":
            rename_and_truncate_jpgs(folder_path)
        else:
            print("Operation cancelled.")

    except FileNotFoundError:
        print(f"Error: Folder not found: {folder_path}")

if __name__ == "__main__":
    main()
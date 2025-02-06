from PIL import Image
import os

def create_pdf_from_images(input_folder, output_pdf):
    images = [os.path.join(input_folder, f) for f in os.listdir(input_folder)
              if f.lower().endswith(('png', 'jpg', 'jpeg'))]
    images.sort()  # Sort to maintain order
    
    if not images:
        print("No images found in the folder.")
        return
    
    page_size = (3300, 2550)  # Set page size to 11 x 8.5 inches at 300 DPI (landscape format)  
    pages = []
    
    for i in range(0, len(images), 4):
        page = Image.new('RGB', page_size, (255, 255, 255))
        quadrants = images[i:i+4]
        
        for idx, img_path in enumerate(quadrants):
            img = Image.open(img_path)
            img_ratio = img.width / img.height
            
            # Compute quadrant position
            quad_w, quad_h = page_size[0] // 2, page_size[1] // 2
            new_w, new_h = quad_w, int(quad_w / img_ratio)
            
            if new_h > quad_h:
                new_h = quad_h
                new_w = int(quad_h * img_ratio)
            
            img = img.resize((new_w, new_h), Image.LANCZOS)
            
            x_offset = (idx % 2) * quad_w + (quad_w - new_w) // 2
            y_offset = (idx // 2) * quad_h + (quad_h - new_h) // 2
            page.paste(img, (x_offset, y_offset))
        
        pages.append(page)
    
    pages[0].save(output_pdf, save_all=True, append_images=pages[1:], resolution=300.0)  # Ensure correct DPI
    print(f"PDF saved as {output_pdf}")

# Set the input folder and output file
input_folder = "turtle_images_internet/"
output_pdf = "output.pdf"
create_pdf_from_images(input_folder, output_pdf)

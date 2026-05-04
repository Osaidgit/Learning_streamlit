from rembg import remove
from PIL import Image
import io

def remove_background(input_path, output_path):
    # 1. Open the image
    with open(input_path, 'rb') as i:
        input_image = i.read()

    # 2. Process the image (this runs the model locally)
    output_image = remove(input_image)

    # 3. Save the result
    with open(output_path, 'wb') as o:
        o.write(output_image)
    
    print(f"Success! Saved to {output_path}")

# Example usage
remove_background('input.jpg', 'output.png')
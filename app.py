from rembg import remove
from PIL import Image
import io
import streamlit as st

st.title("Background Removal App")
st.write("Upload an image to remove its background.")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Read the uploaded image
    input_image = uploaded_file.read()
    
    # Process the image to remove the background
    output_image = remove(input_image)
    
    # Display the result
    st.image(output_image, caption='Processed Image', use_column_width=True)
    st.button("Upload Image")

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
import os
from PIL import Image
from pathlib import Path
import pillow_heif

# Register HEIF opener with PIL
pillow_heif.register_heif_opener()

def resize_image(image_path, output_path, target_size=1024):
    """
    Resize image so its shortest side is target_size pixels while maintaining aspect ratio
    """
    with Image.open(image_path) as img:
        # Convert HEIF images to RGB mode
        if img.format == 'HEIF':
            img = img.convert('RGB')
        
        # Get original dimensions
        width, height = img.size
        
        # Calculate new dimensions
        if width < height:
            # Width is shorter side
            new_width = target_size
            new_height = int(height * (target_size / width))
        else:
            # Height is shorter side
            new_height = target_size
            new_width = int(width * (target_size / height))
        
        # Resize image
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Save resized image - convert HEIF to JPEG
        if image_path.suffix.lower() in {'.heif', '.heic'}:
            output_path = output_path.with_suffix('.jpg')
        resized_img.save(output_path, quality=95)

def process_folder(input_folder):
    """
    Process all images in the input folder and save resized versions
    """
    # Create output folder name by adding '_resized'
    input_path = Path(input_folder)
    output_folder = input_path.parent / f"{input_path.name}_resized"
    
    # Create output folder if it doesn't exist
    output_folder.mkdir(exist_ok=True)
    
    # Supported image extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.heif', '.heic'}
    
    # Process each file in the input folder
    for file_path in input_path.iterdir():
        if file_path.suffix.lower() in image_extensions:
            # Create output path
            output_path = output_folder / file_path.name
            
            try:
                resize_image(file_path, output_path)
                print(f"Processed: {file_path.name}")
            except Exception as e:
                print(f"Error processing {file_path.name}: {str(e)}")

if __name__ == "__main__":
    # Get input folder from user
    input_folder = input("Enter the path to the folder containing images: ")
    
    # Process the folder
    if os.path.isdir(input_folder):
        process_folder(input_folder)
        print("\nProcessing complete!")
    else:
        print("Invalid folder path. Please provide a valid folder path.")

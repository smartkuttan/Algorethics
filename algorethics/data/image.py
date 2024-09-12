from PIL import Image
import io

def process_image_data(image_path):
    """
    Processes image data for validation.

    Parameters:
    - image_path (str): Path to the image file.

    Returns:
    - Image: Processed image object.
    """
    # Load image
    image = Image.open(image_path)
    
    # Resize image for consistency
    image = image.resize((256, 256))
    
    # Convert image to grayscale, if necessary
    image = image.convert('L')  # Convert to grayscale
    
    return image

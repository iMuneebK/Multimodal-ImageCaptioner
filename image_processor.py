from PIL import Image
import io
import typing as t

def process_uploaded_image(uploaded_file) -> Image.Image:
    """
    Process an uploaded file from Streamlit into a PIL Image.
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        
    Returns:
        PIL Image converted to RGB
    """
    image_bytes = uploaded_file.getvalue()
    image = Image.open(io.BytesIO(image_bytes))
    
    if image.mode != "RGB":
        image = image.convert("RGB")
        
    return image

def resize_image_for_display(image: Image.Image, max_width: int = 800) -> Image.Image:
    """
    Resize image proportionally for UI display purposes to save memory.
    
    Args:
        image: PIL Image
        max_width: Maximum width in pixels
        
    Returns:
        Resized PIL Image
    """
    if image.width > max_width:
        ratio = max_width / image.width
        new_height = int(image.height * ratio)
        return image.resize((max_width, new_height), Image.Resampling.LANCZOS)
    return image

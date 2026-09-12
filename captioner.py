import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import typing as t

from config import MODEL_NAME, DEVICE, MAX_LENGTH, MIN_LENGTH, STYLES

class ImageCaptioner:
    """Handles loading the BLIP model and generating captions."""
    
    def __init__(self, model_name: str = MODEL_NAME, device: str = DEVICE):
        self.device = device
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name).to(self.device)

    def generate_caption(self, image: Image.Image, style: str = "Descriptive") -> str:
        """
        Generate a caption for a single image.
        
        Args:
            image: PIL Image object
            style: One of the predefined styles for caption refinement
            
        Returns:
            String containing the generated caption
        """
        text_prompt = ""
        if style == "Creative":
            text_prompt = "A beautiful and creative photo of"
        elif style == "Technical":
            text_prompt = "A technical overview showing"
        
        inputs = self.processor(image, text_prompt, return_tensors="pt").to(self.device)
        
        out = self.model.generate(
            **inputs, 
            max_length=MAX_LENGTH,
            min_length=MIN_LENGTH
        )
        
        caption = self.processor.decode(out[0], skip_special_tokens=True)
        return caption.capitalize()
        
    def generate_batch_captions(self, images: t.List[Image.Image], style: str = "Descriptive") -> t.List[str]:
        """Generate captions for a batch of images."""
        return [self.generate_caption(img, style) for img in images]

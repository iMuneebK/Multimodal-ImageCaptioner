# AI Image Captioning System Configuration

# Model settings
MODEL_NAME = "Salesforce/blip-image-captioning-base"
DEVICE = "cpu" # Set to 'cuda' if GPU is available
MAX_LENGTH = 50
MIN_LENGTH = 10

# Application settings
APP_TITLE = "AI Image Captioning Studio"
APP_DESCRIPTION = "Upload images to generate intelligent, context-aware captions using BLIP models."

# Styling settings
STYLES = {
    "Descriptive": "Provide a literal and highly descriptive caption.",
    "Creative": "Provide a creative, artistic, and poetic caption.",
    "Technical": "Provide a highly technical, objective, and precise caption."
}

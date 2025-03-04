from PIL import Image
import requests
from io import BytesIO

def load_image_from_path(image_path):
    """Loads an image from a local file path."""
    return Image.open(image_path)

def load_image_from_url(image_url):
    """Fetches and loads an image from a URL."""
    response = requests.get(image_url)
    return Image.open(BytesIO(response.content))

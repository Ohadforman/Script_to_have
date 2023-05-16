import pytesseract
from PIL import Image

def read_text_from_image(image_path):
    # Open the image file
    image = Image.open(image_path)
    
    # Convert the image to grayscale
    image = image.convert("L")
    
    # Apply OCR using Tesseract
    text = pytesseract.image_to_string(image)
    
    # Print the extracted text
    print(text)

# Replace "image_path.jpg" with the path to your image file
read_text_from_image("/Users/ohadformanair/Downloads/EXP78_photos/AMP2SHARP.jpg")

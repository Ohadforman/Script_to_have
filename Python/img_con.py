from PIL import Image, ImageEnhance

# Load the original image
image_file = "/Users/ohadformanair/Documents/Python/AMAN_im.jpeg"
image = Image.open(image_file)

# Create an enhancer object and adjust the contrast
enhancer = ImageEnhance.Contrast(image)
enhanced_image = enhancer.enhance(0.5)  # Increase contrast by a factor of 1.5

# Convert the image to black and white
bw_image = enhanced_image.convert("L")  # L mode converts the image to grayscale

# Save the modified image to a new file
bw_image.save("/Users/ohadformanair/Documents/Python/AMAN_immodified_image.jpg")

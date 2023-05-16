import cv2
import numpy as np

def sharpen_image(image_path, output_path, strength=1.5, radius=1, threshold=0):


    # Load the image
    image = cv2.imread(image_path)

    # Apply the unsharp mask
    blurred = cv2.GaussianBlur(image, (0, 0), radius)
    sharpened = cv2.addWeighted(image, 1 + strength, blurred, -strength, 0)
    sharpened = cv2.threshold(sharpened, threshold, 255, cv2.THRESH_TOZERO)[1]

    # Save the sharpened image
    cv2.imwrite(output_path, sharpened)

    print("Image sharpening complete.")

    """
    Apply sharpening effect to an image using an unsharp mask.

    Parameters:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the sharpened image file.
        strength (float, optional): Strength of the sharpening effect. Default is 1.5.
        radius (int, optional): Radius for Gaussian blur. Default is 1.
        threshold (int, optional): Threshold for sharpening. Default is 0.

    Returns:
        None
    """


image_path = '/Users/ohadformanair/Downloads/EXP78_photos/coupler.jpeg'
output_path = 'coup.jpg'

sharpen_image(image_path, output_path, strength=3, radius=3, threshold=0)

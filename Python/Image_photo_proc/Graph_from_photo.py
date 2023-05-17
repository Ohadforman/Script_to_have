import cv2
import numpy as np
import os

def mark_yellow_dots(image_path, y_offset):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for yellow color in HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    # Create a mask for yellow color
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Put a dot on each yellow dot
    for contour in contours:
        for point in contour:
            x, y = point[0]
            # Add y_offset to the y-coordinate of the red dot
            cv2.circle(image, (x, y + y_offset), 1, (0, 0, 255), -1)

    # Get the file name from the input image path
    file_name = os.path.basename(image_path)

    # Set the output path in the destination directory
    output_path = os.path.join(destination_directory, file_name + '_adjusted.png')

    # Save the modified image
    cv2.imwrite(output_path, image)

def process_directory(source_directory, destination_directory, y_offset):
    # Create the destination directory if it doesn't exist
    os.makedirs(destination_directory, exist_ok=True)

    # Get a list of all files in the source directory
    file_list = os.listdir(source_directory)

    # Process each image file
    for file_name in file_list:
        # Check if the file is an image (with supported extensions)
        if file_name.endswith(('.png', '.jpg', '.jpeg')):
            # Construct the image path
            image_path = os.path.join(source_directory, file_name)

            # Call the function to mark the yellow dots and save the modified image
            mark_yellow_dots(image_path, y_offset)

# Specify the source directory
source_directory = '/Users/ohadformanair/Documents/Git/AML/LAB_7p8/DATA7'

# Specify the destination directory
destination_directory = '/Users/ohadformanair/Documents/Git/AML/LAB_7p8/DATA7/Adjusted'

# Specify the y-axis offset for the red dots
y_offset = -115

# Call the function to process the directory and mark yellow dots in all images
process_directory(source_directory, destination_directory, y_offset)

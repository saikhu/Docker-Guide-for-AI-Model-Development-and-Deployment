import cv2

# Load an image
image = cv2.imread('sample.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the processed image
success = cv2.imwrite('/usr/src/app/output/gray_image.jpg', gray_image)

if success:
    print("Image successfully saved.")
else:
    print("Error: Image not saved.")
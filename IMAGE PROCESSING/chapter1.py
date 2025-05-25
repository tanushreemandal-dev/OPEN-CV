# import cv2
# import matplotlib.pyplot as plt

# # Read the image using OpenCV (in BGR format)
# img = cv2.imread("IMAGE PROCESSING/Capture 1.PNG", cv2.IMREAD_COLOR)

# # Check if image is loaded properly
# if img is None:
#     print("Error: Image not found or failed to load.")
# else:
#     # Convert BGR to RGB (for proper display in matplotlib)
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#     # Display the image using matplotlib
#     plt.imshow(img_rgb)
#     plt.title("Image Display - geeksforgeeks.png")
#     plt.axis('off')  # Hide axes
#     plt.show()
import cv2

img = cv2.imread("IMAGE PROCESSING/Capture 1.PNG")

if img is None:
    print("Error: Image not found or failed to load.")
else:
    cv2.imwrite("output_image.png", img)
    print("Image saved as output_image.png")

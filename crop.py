import cv2

# Step 1: Load the image
img = cv2.imread('your_image.png')

# Step 2: Define crop region (top-left corner: x1, y1, bottom-right corner: x2, y2)
x1, y1 = 100, 100
x2, y2 = 200, 200

# Step 3: Crop the region
cropped = img[y1:y2, x1:x2]

# Step 4: Modify the cropped image (e.g., invert colors)
modified_cropped = 255 - cropped  # Simple invert

# Step 5: Put it back
img[y1:y2, x1:x2] = modified_cropped

# Step 6: Save or display the result
cv2.imwrite('final_image.png', img)
# Or to view it:
# cv2.imshow('Result', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

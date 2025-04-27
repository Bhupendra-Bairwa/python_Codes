# TASK 1: Image Handling

# pip inatall opencv-python
import cv2

# Step 1: Capture an image using the webcam
cap = cv2.VideoCapture(0)  # 0 is usually the default webcam

print("Press 'c' to capture the image.")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Webcam", frame)

    k = cv2.waitKey(1)
    if k % 256 == ord('c'):  # Press 'c' to capture
        captured_image = frame.copy()
        break

cap.release()
cv2.destroyAllWindows()

# Step 2: Save the captured image
save_path = "captured_image.jpg"
cv2.imwrite(save_path, captured_image)
print(f"Image saved at {save_path}")

# Step 3: Display the saved image
img = cv2.imread(save_path)
cv2.imshow("Captured Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 4: Edit the image (example: crop the center part)
# Get the image dimensions
h, w, _ = img.shape
start_row, start_col = int(h * 0.25), int(w * 0.25)
end_row, end_col = int(h * 0.75), int(w * 0.75)

# Crop the image
cropped_img = img[start_row:end_row, start_col:end_col]

# Modify pixels (example: set top-left 50x50 region to red)
cropped_img[0:50, 0:50] = [0, 0, 255]  # BGR format (red)

# Display the edited image
cv2.imshow("Edited Image", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optionally save the edited image
cv2.imwrite("edited_image.jpg", cropped_img)
print("Edited image saved as edited_image.jpg")

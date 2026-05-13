import cv2
import numpy as np
image = cv2.imread("input.jpg")
ke = 50
encrypted = image + ke
cv2.imwrite("encryption.jpg", encrypted)
print("Image Encrypted Successfully!")
decrypted = encrypted - ke
cv2.imwrite("decrypted.jpg", decrypted)
print("Image Decrypted Successfully!")

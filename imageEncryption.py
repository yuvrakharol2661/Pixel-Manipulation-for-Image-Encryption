import cv2
import numpy as np
image = cv2.imread("input.jpg")
key = 50
encrypted = image + key
cv2.imwrite("encryption.jpg", encrypted)
print("Image Encrypted Successfully!")
decrypted = encrypted - key
cv2.imwrite("decrypted.jpg", decrypted)
print("Image Decrypted Successfully!")

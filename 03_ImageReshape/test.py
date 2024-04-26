import cv2

img = cv2.imread("test.jpg")
cv2.imshow("image", img)

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
 
k = cv2.waitKey(0)
cv2.destroyAllWindows()
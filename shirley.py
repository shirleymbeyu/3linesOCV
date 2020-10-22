import cv2
img =cv2.imread('sweetpotatoes.jpg', 0)
print(img)

cv2.imshow('sweetpotatoes',img)
cv2.waitKey(20000)
cv2.destroyAllWindows()

import cv2

img = cv2.imread('red.jpg')
img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)   # this code line is for resizing large images.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow('final output', cartoon)
cv2.waitKey(0)

# Destroying present windows on screen
cv2.destroyAllWindows()

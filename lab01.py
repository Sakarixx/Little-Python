import cv2

# read image
image = cv2.imread('image/lab.jpg')
imageresize = cv2.resize(image, (500,500))
# show the image, provide window name first
cv2.imshow('Panwasa 056350201003-3', image)
cv2.waitKey(delay=10000)
cv2.destroyAllWindows()
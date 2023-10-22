import cv2
image = cv2.imread('image/lab.jpg')

n1 = cv2.resize(image,(500,650))

cv2.arrowedLine(n1, (0, 0), (500, 0), (179, 94, 255), 20)
cv2.arrowedLine(n1, (500, 0), (500, 650), (231, 114, 255), 20)
cv2.arrowedLine(n1, (500, 650), (0, 650), (255, 96, 154), 20)
cv2.arrowedLine(n1, (0, 650), (0, 00), (255, 209, 82), 20)

cv2.circle(n1, (250, 325), 250, (8, 107, 206), 10)
cv2.circle(n1, (250, 325), 125, (161, 219, 255), 10)
cv2.imshow('Panwasa 056350201003-3',n1)

cv2.waitKey(delay=100000)
cv2.destroyAllWindows

import cv2
import numpy

image = cv2.imread('imagevideo/View01.jpg', 0)
image = cv2.resize(image, (500, 450))

imageColor = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

cv2.rectangle(imageColor, (3, 3), (500, 450), (227, 125, 255), 5)
cv2.circle(imageColor, (250, 225), 150, (250, 37, 80), 5)
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(imageColor, 'RMUTP', (150, 230), font,2, (255, 0, 128), 2, cv2.LINE_AA)

cv2.imshow('PANWASA PASANAE', imageColor)
cv2.waitKey(0)
cv2.destroyAllWindows()

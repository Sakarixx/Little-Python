import cv2
import numpy

imggmn = cv2.imread('imagevideo/Rilakkuma.jpg')

imageresize = cv2.resize(imggmn, (500, 450))

points = []


def clickPosition(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imggmn, (x, y), 10, (101, 77, 183), 5)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(imggmn, points[-2], points[-1], (0, 0, 255), 5)
        cv2.imshow("05630201003-3 Panwasa", imggmn)
       
        cv2.putText(imggmn, "Valentine", (75, 500),
        cv2.FONT_HERSHEY_DUPLEX, 5, (194, 118, 217), cv2.LINE_8)


# แสดงภาพ
cv2.imshow("05630201003-3 Panwasa", imggmn)
# ทางานกับ Mouse
cv2.setMouseCallback("05630201003-3 Panwasa", clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()

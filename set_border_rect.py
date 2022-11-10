from icecream import ic
import cv2

rect_color = (0,0,0)
line_thickness = 4
camera = cv2.VideoCapture(0)

ret, frame = camera.read()
hight, width = frame.shape[:2]
left_late = 0
top_late = 0.4
right_late = 1
bottom_late = 1
cv2.rectangle(frame, (int(width*left_late), int(hight*top_late)), (int(width*right_late), int(hight*bottom_late)), rect_color)
cv2.imshow("CAM", frame)
cv2.waitKey()

camera.release()
cv2.destroyAllWindows()
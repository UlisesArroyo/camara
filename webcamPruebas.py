from cv2 import *
namedWindow("webcam2")
namedWindow("webcam")
vc = VideoCapture(2);

while True:
    next, frame = vc.read()

    gray = cvtColor(frame, COLOR_BGR2GRAY)
    gauss = GaussianBlur(gray, (7,7), 1.5, 1.5)
    can = Canny(gauss, 0, 30, 3)

    imshow("webcam", can)
    imshow("webcam2", frame)
    if waitKey(50) >= 0:
        break;
import cv2
from fpdf import FPDF
import os

url = "http://192.168.0.100:8080/video"
cap = cv2.VideoCapture(url)
ret = True
f1 = 0
i = 0
while ret:
    ret, frame = cap.read()
    if f1 == 0:
        print("press 's' to scan the document")
        print("press 'q' to quit")
        f1 = f1 + 1

    cv2.imshow("camera feed", frame)
    k = cv2.waitKey(1)  
    if k == ord('s'):
        cv2.destroyWindow("camera feed")
        cv2.imshow("Scanned photo", frame)
        print("press u if its unreadable")
        print("press b to convert it to black and white form")
        print("press l to see in dark mode")
        k1 = cv2.waitKey(0)
        if k1 == ord('u'):
            cv2.destroyWindow('Scanned photo')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            new = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)
            cv2.imwrite("D://PDF//scanned%d.jpg" % i, new)
            i = i + 1
            print("press 's' to scan more document")
            print("press 'q' to quit")
            continue
        elif k1 == ord('b'):
            cv2.destroyWindow('Scanned photo')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite("D://PDF//scanned%d.jpg" % i, gray)
            i = i + 1
            print("press 's' to scan more document")
            print("press 'q' to quit")
            continue
        elif k1 == ord('l'):
            cv2.destroyWindow('Scanned photo')
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            laplacian = cv2.Laplacian(frame, cv2.CV_64F)


            cv2.imwrite("D://PDF//scanned%d.jpg" % i, laplacian)
            i = i + 1
            print("press 's' to scan more document")
            print("press 'q' to quit")
            continue

    elif k == ord('q'):
        ret = False
        break

cv2.destroyAllWindows()
imagelist = os.listdir("D://PDF//")
pdf = FPDF()
for image in imagelist:
    image = "D://PDF//" + image
    pdf.add_page()
    width = 210
    height = 297
    pdf.image(image,0,0,width,height)
pdf.output("D://PDF//your_file.pdf", "F")

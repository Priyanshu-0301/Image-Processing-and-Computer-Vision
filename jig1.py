import numpy as np
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

cv.namedWindow('Point Coordinates')

def click_event(event, x, y, flags, params):
   if event == cv.EVENT_LBUTTONDOWN:
      print(f'({x},{y})')
      cv.putText(img, f'({x},{y})',(x,y),
      cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
      cv.circle(img, (x,y), 3, (0,255,255), -1) 

# from google.colab import files
# upload = files.upload();
img = cv.imread(r'jigsaw.jpg')

cv.setMouseCallback('Point Coordinates', click_event)
while True:
   cv.imshow('Point Coordinates',img)
   k = cv.waitKey(1) & 0xFF
   if k == 27:
      break
cv.destroyAllWindows()


sub_img1 = img[150:330, 515:700]
sub_img1 = cv.flip(sub_img1, 1)

img[150:330, 515:700] = sub_img1

sub_img2 = img[370:420, 370:795]
sub_img2 = cv.flip(sub_img2, 0)

img[370:420, 370:795] = sub_img2

sub_img3 = img[0:200, 0:190]


sub_img4 = img[200:410, 0:190]
sub_img4 = cv.flip(sub_img4, 0)

img[200:400, 0:190] = sub_img3
img[0:210, 0:190] = sub_img4

plt.axis('off')
plt.imshow(img)
plt.show()
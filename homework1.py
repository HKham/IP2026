import cv2
import numpy as np

drawing = False 
ix, iy = -1, -1
cx, cy = -1, -1

org_img = cv2.imread('hamster2.jpg')
img = org_img.copy() 

alpha = 0.4  

def nothing(x):
    pass

def draw_rectangle(event,x,y,flags,param):
    global ix, iy, cx, cy, drawing, org_img

    if event == cv2.EVENT_LBUTTONDOWN :
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        cx, cy = x, y
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cx, cy = x, y

        overlay = org_img.copy()
        cv2.rectangle(overlay, (ix,iy), (cx,cy), (0,255,0), -1)
        cv2.addWeighted(overlay, alpha, org_img, 1 - alpha, 0, org_img)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.createTrackbar('Value','image',0,255,nothing)
cv2.setMouseCallback('image', draw_rectangle)
font = cv2.FONT_HERSHEY_SIMPLEX

while(1) :
    img = org_img.copy() 
    value = cv2.getTrackbarPos('Value', 'image')

    if drawing == True: 
        overlay = img.copy()
        cv2.rectangle(overlay, (ix,iy), (cx,cy),(0,255,0), -1)
        cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)


    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
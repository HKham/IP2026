import cv2
import numpy as np

drawing = False 
ix, iy = -1, -1

def nothing(x):
    pass

def draw_rectangle(event,x,y,flags,param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN :
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix,iy), (x,y), (0, 255, 0), -1)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix,iy), (x,y), (0, 255,0), -1)

org_img = cv2.imread('hamster2.jpg')
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.createTrackbar('Value','image',0,255,nothing)
cv2.setMouseCallback('image', draw_rectangle)
font = cv2.FONT_HERSHEY_SIMPLEX


###



while(1) :
    img = org_img.copy() 
    value = cv2.getTrackbarPos('Value', 'image')
    cv2.putText(img,f'Mouse position: {value}',(10,30), font, 1,(255,255,255),1,cv2.LINE_AA)

    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
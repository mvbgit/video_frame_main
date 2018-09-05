import cv2
import numpy as np
import imutils


def nothing(x):
    pass


cv2.namedWindow('result')

cap = cv2.VideoCapture(0)

while(1):
    _, img = cap.read()
    img = cv2.medianBlur(img,3)

    result=img.copy()
    
    #############################in the mean time a what colour is this note
    t=img[240,320]      
    txt=str(t[0])+" "+str(t[1])+" "+str(t[2])
    cv2.putText(img,txt, (40,100), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,255),2)
    cv2.circle(img,(320,240), 10, (0,0,255),2)

    
    #wide=30 # how wide a spread of looking 30 seems ok not use d in BGR used in LAB
    
    maskr = cv2.inRange(img, (-1,0,0), (-1, 0,0)) #blank start
    maskb = maskr.copy()
    maskg = maskr.copy()
    masky = maskr.copy()
    masko = maskr.copy()
    maskwh = maskr.copy()
    maskgr = maskr.copy()
    maskbl = maskr.copy()
    for i in range(5, 251, 5):
        maskr+=cv2.inRange(img, (0,0,i), (i/5, i/5,i+5)) #red
        maskb+=cv2.inRange(img, (i,0,0), (i+5, i/5,i/5)) #blue
        maskg+=cv2.inRange(img, (0,i,0), (i/5, i+5,i/5)) #green
        masko+=cv2.inRange(img, (0,i/10,i), (i/5, i-i/3,i+5)) #orange is tricky whatch it take over yellow
        masky+=cv2.inRange(img, (0,i-i/3,i-i/3), (i/5, i+5,i+5)) #yellow
        if i>150:
            maskwh+=cv2.inRange(img, (150,150,150), (i+5,i+5,i+5)) #white/grey/black
        elif i>50:
            maskgr+=cv2.inRange(img, (55,55,55), (i+5, i+5,i+5)) #white/grey/black
        else:
            maskbl+=cv2.inRange(img, (0,0,0), (i+5, i+5,i+5)) #white/grey/black

    #do something special for white grgey black all similar but intensity  is white or grey or black  
    #maskwgb+=cv2.inRange(img, (i-i/3,i-i/3,i-i/3), (i+5, i+5,i+5)) #white/grey/black

        
    back=img.copy()
    back[:,:,0]=0
    back[:,:,1]=0
    back[:,:,2]=255
    red    = cv2.bitwise_and(back,back,mask = maskr)
    back[:,:,0]=255
    back[:,:,1]=0
    back[:,:,2]=0
    blue    = cv2.bitwise_and(back,back,mask = maskb)
    back[:,:,0]=0
    back[:,:,1]=255
    back[:,:,2]=0
    green   = cv2.bitwise_and(back,back,mask = maskg)
    back[:,:,0]=0
    back[:,:,1]=100
    back[:,:,2]=255
    orange   = cv2.bitwise_and(back,back,mask = masko) 
    back[:,:,0]=0
    back[:,:,1]=255
    back[:,:,2]=255
    yellow   = cv2.bitwise_and(back,back,mask = masky)


    
    back[:,:,0]=255
    back[:,:,1]=255
    back[:,:,2]=255
    white   = cv2.bitwise_and(back,back,mask = maskwh)
    back[:,:,0]=125
    back[:,:,1]=125
    back[:,:,2]=125
    grey   = cv2.bitwise_and(back,back,mask = maskgr)
    back[:,:,0]=0
    back[:,:,1]=0
    back[:,:,2]=0
    black   = cv2.bitwise_and(back,back,mask = maskbl)

    result=red+blue+green+yellow+orange+white+grey+black #grey white and black do go but worry me


    cv2.imshow("img",img)

    #blur3 = cv2.medianBlur(result,3)
    #cv2.imshow("blur3",blur3)

    #blur5 = cv2.medianBlur(result,5)
    #cv2.imshow("blur5",blur5)


    
 
    cv2.imshow("result",result) # to get this width thing going
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

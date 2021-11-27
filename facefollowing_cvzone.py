from djitellopy import tello
import cv2
from cvzone.FaceDetectionModule import FaceDetector
import cvzone


# cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
detector = FaceDetector(minDetectionCon=0.7)
# _,img = cap.read()
hi,wi =480,640
# hi , wi = img.shape[0],img.shape[1]

xPID = cvzone.PID([.22,0,0.1],wi//2)
yPID = cvzone.PID([.27,0,0.1],hi//2,axis=1)
zPID = cvzone.PID([.003,0,0.003],12000,limit=[-20,13])
myplotX = cvzone.LivePlot(yLimit=[-100,100],char='X')
myplotY = cvzone.LivePlot(yLimit=[-100,100],char='Y')
myplotZ = cvzone.LivePlot(yLimit=[-100,100],char='Z')

me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamoff()
me.streamon()
me.takeoff()
me.move_up(80)


while True:
    # _,img = cap.read()
    bat =me.get_battery()
    img = me.get_frame_read().frame
    img = cv2.resize(img,(640,480))
    img , bboxs = detector.findFaces(img , draw=True)
   
    if bboxs:
        cx,cy = bboxs[0]['center']
        x , y, w, h = bboxs[0]['bbox']
        area = w*h
        # print(area)

        xVal =int(xPID.update(cx))
        yVal =int(yPID.update(cy))
        zVal =int(zPID.update(area))


        
        imgPlotX = myplotX.update(xVal)
        imgPlotY = myplotY.update(yVal)
        imgPlotZ = myplotZ.update(zVal)

        
        # cv2.putText(img,str(xVal),(50,100),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        img = xPID.draw(img,[cx,cy])
        img = yPID.draw(img,[cx,cy])

        # cv2.circle(img , (cx,cy),5,(255,0,255),cv2.FILLED)
        # error = wi//2-cx
        cv2.putText(img,(str(bat)),(50,100),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),3)
        # cv2.line(img , (wi//2,0),(wi//2,hi),(255,0,0),2)
        # cv2.line(img,(wi//2,hi//2),(cx,cy),(255,0,255),3)
    imgStacked =cvzone.stackImages([img,imgPlotY,imgPlotZ],2,0.7)
    me.send_rc_control(0,-zVal,-yVal,xVal)

    cv2.imshow('imgStacked',imgStacked)
    # cv2.imshow('OUTPUT',img)
    # cv2.imshow('imgPlotx',imgPlotX)
    if cv2.waitKey(5) & 0xff==('q'):
        # me.land()
        break
cv2.destroyAllWindows
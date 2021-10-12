import kepressmodule as kp
from djitellopy import tello
from time import sleep
import numpy as np
import cv2
import math

## PARAMETERS
fSpeed = 117/18 #forward speed cm/s actual(15 cm/s)
aSpeed = 360/10 # angilar speed Degree/s
Interval = 0.25
dInterval = fSpeed*Interval
aInterval = aSpeed*Interval
###################
x,y=500,500
a=0
yaw = 0
points= []

kp.init()
me = tello.Tello()

me.connect()
print(me.get_battery())



def getKeyBoardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 15
    aspeed = 50
    d = 0
    global yaw, x, y, a

    if kp.getKey("LEFT") :
         lr = -speed
         d = dInterval
         a = -180
    elif kp.getKey("RIGHT") :
         lr = speed
         d = -dInterval
         a = 180


    if kp.getKey("UP") :
         fb = speed
         d = dInterval
         a = 270

    elif kp.getKey("DOWN") : 
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getKey("w") : ud = speed
    elif kp.getKey("s") : up = -speed

    if kp.getKey("a"):
         yv = aspeed
         yaw -= aInterval
    if kp.getKey("d"):
         yv = -aspeed
         yaw+=aInterval 

    if kp.getKey("q"):  me.land()
    if kp.getKey("t"): me.takeoff()
    sleep(Interval)

    a+=yaw
    x+=int(d*math.cos(math.radians(a)))
    y+=int(d*math.sin(math.radians(a)))




    return [lr, fb, ud, yv ,x , y]

def drawPoints(img , points):
    for point in points:
        cv2.circle(img,(point[0],point[1]),5,(0,0,255),cv2.FILLED)
    cv2.circle(img,(points[-1]),5,(255,0,255),cv2.FILLED)
    cv2.putText(img, f'({(points[-1][0] - 500)/100},{(points[-1][1]-500)/100})m',(points[-1][0]+10,points[-1][1]+30),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),1)




while True:
    vals = getKeyBoardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = np.zeros((1000,1000,3),np.uint8)
    points.append((vals[4],vals[5]))
    drawPoints(img , points)
    cv2.imshow("OUTPUT",img)
    cv2.waitKey(1)



import kepressmodule as kp
from djitellopy import tello
from time import sleep
import time
import cv2
global img


kp.init()
me = tello.Tello()

me.connect()
print(me.get_battery())
me.streamon()


def getKeyBoardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    

    if kp.getKey("LEFT") : lr = -speed
    elif kp.getKey("RIGHT") : lr = speed

    if kp.getKey("UP") : fb = speed
    elif kp.getKey("DOWN") : fb = -speed

    if kp.getKey("w") : ud = speed
    elif kp.getKey("s") : up = -speed

    if kp.getKey("a"): yv = speed
    if kp.getKey("d"): yv = -speed 

    if kp.getKey("q"):  me.land()
    if kp.getKey("t"): me.takeoff()

    if kp.getKey('z'):
        cv2.imwrite(f'D:\python\python_dsa\python_quad\Resources\Images\{time.time()}.jpg', img)
        sleep(.5)


    return [lr, fb, ud, yv ]




while True:
    vals = getKeyBoardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    # img = cv2.resize(img,(360,240))
    cv2.imshow("imgae", img)
    cv2.waitKey(1)
   


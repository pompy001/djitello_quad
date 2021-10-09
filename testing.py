from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())
me.takeoff()
me.query_distance_tof()
me.send_rc_control(0, 50, 0, 0)
sleep(1)
me.query_distance_tof()
me.send_rc_control(0, 0, 0, 0)
me.land()
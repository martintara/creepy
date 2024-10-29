# main.py

from creepy_pod import CreepyPod
from creepy_state import CreepyState
from maestro import Controller
import maestro
from didleg import Leg
import time
from display import *
from servo import Servo

def main():
    # testing av leg objekter, har testet leg 0 og 1)
    ctrl = maestro.Controller()
 
    servo_list0 = [
        Servo(ctrl, 0, 5400, 950, 0, 45),
        Servo(ctrl, 1, 6125, 3775, 0, 45),
        Servo(ctrl, 2, 4850, 3250, 0, 45)
                    ]


    servo_list1 = [
            Servo(ctrl, 3, 6025, 950, 90, 90),
        Servo(ctrl, 4, 6400, 3775, 90, 90),
        Servo(ctrl, 5, 5125, 3250, 90, 90)
                   ]

    servo_list2 = [
        Servo(ctrl, 6, 6400, 2350, 90, 90),
        Servo(ctrl, 7, 6450, 3775, 90, 90),
        Servo(ctrl, 8, 5050, 3250, 90, 90)
                   ]

    servo_list3 = [
        Servo(ctrl, 9, 5750, 2350, 90, 90),
        Servo(ctrl, 10, 5875, 3775, 90, 90),
        Servo(ctrl, 11, 5200, 3250, 90, 90)
            ]

    servo_list4 = [
        Servo(ctrl, 12, 5600, 2350, 90, 90),
        Servo(ctrl, 13, 6400, 3775, 90, 90),
        Servo(ctrl, 14, 5025, 3250, 90, 90)
                   ]

    servo_list5 = [
        Servo(ctrl, 15, 5000, 2350, 90, 90),
        Servo(ctrl, 16, 6250, 3775, 90, 90),
        Servo(ctrl, 17, 5025, 3250, 90, 90)
                   ]




    leg0 = Leg(ctrl, 0, servo_list0)
    leg1 = Leg(ctrl, 1, servo_list1)

#    leg0.standby_position()
#    time.sleep(5)
#    leg0.initial_position()
    startup()
    leg0.initial_position()
    leg1.initial_position()
    time.sleep(2)
#    leg0.standby_position()
#    time.sleep(3)
    idle()
    leg0.lower_leg1()
    leg1.lower_leg1()
    time.sleep(3)
#    leg0.initial_position()
    leg1.rotate_forward()
    leg0.rotate_backward()
    time.sleep(3)
    leg0.rotate_forward()
    leg1.rotate_backward()
    time.sleep(3)
#    leg0.lower_leg1()
#    time.sleep(3)
#    leg0.rotate_backward()
#    time.sleep(3)
#    leg0.initial_position()


if __name__ == "__main__":
    main()

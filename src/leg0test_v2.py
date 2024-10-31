# main.py

from creepy_pod import CreepyPod
from creepy_state import CreepyState
from maestro import Controller
import maestro
from leg import Leg
import time

from servo import Servo

def main():
    # testing av leg objekter, har testet leg 0 og 1)
    ctrl = maestro.Controller()
 
    servo_list0 = [
        Servo(ctrl, 0, 5900, 2350, 0, 45),
        Servo(ctrl, 1, 6125, 3775, 0, 45),
        Servo(ctrl, 2, 5100, 3000, 0, 70)
                    ]


    servo_list1 = [
        Servo(ctrl, 3, 6025, 2350, 90, 90),
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
#   leg1 = Leg(ctrl, 1, servo_list1)
    leg0.initial_position()

    leg0.manual_control_angle(2)
#    leg0.manual_control(1)

if __name__ == "__main__":
    main()

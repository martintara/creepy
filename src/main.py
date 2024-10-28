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
        Servo(ctrl, 0, 5900, 2350),
        Servo(ctrl, 1, 6125, 3775),
        Servo(ctrl, 2, 4850, 3250)
                    ]


    servo_list1 = [
        Servo(ctrl, 3, 6025, 2350),
        Servo(ctrl, 4, 6400, 3775),
        Servo(ctrl, 5, 5125, 3250)
                   ]

    servo_list2 = [
        Servo(ctrl, 6, 6400, 2350),
        Servo(ctrl, 7, 6450, 3775),
        Servo(ctrl, 8, 5050, 3250)
                   ]

    servo_list3 = [
        Servo(ctrl, 9, 5750, 2350),
        Servo(ctrl, 10, 5875, 3775),
        Servo(ctrl, 11, 5200, 3250)
            ]

    servo_list4 = [
        Servo(ctrl, 12, 5600, 2350),
        Servo(ctrl, 13, 6400, 3775),
        Servo(ctrl, 14, 5025, 3250)
                   ]

    servo_list5 = [
        Servo(ctrl, 15, 5000, 2350),
        Servo(ctrl, 16, 6250, 3775),
        Servo(ctrl, 17, 5025, 3250)
                   ]




    leg0 = Leg(ctrl, 0, servo_list0)
    leg1 = Leg(ctrl, 1, servo_list1)
    leg2 = Leg(ctrl, 2, servo_list2)
    leg3 = Leg(ctrl, 3, servo_list3)
    leg4 = Leg(ctrl, 4, servo_list4)
    leg5 = Leg(ctrl, 5, servo_list5)
#    leg1 = Leg(ctrl, 1, 3, 4, 5, 3450, 8600, 2700, 10100, 1650, 8600)
#    leg2 = Leg(ctrl, 2, 6, 7, 8, 4500, 8300, 2600, 10300, 1600, 8500)
#    leg3 = Leg(ctrl, 3, 9, 10, 11, 3800, 7700, 2150, 9600, 1600, 8800)
#    leg4 = Leg(ctrl, 4, 12, 13, 14, 3400, 7800, 2550, 10250, 1600, 8450)
#    leg5 = Leg(ctrl, 5, 15, 16, 17, 3000, 7000, 2500, 10000, 1600, 8450)

    leg0.initial_position()
    leg1.initial_position()
    leg2.initial_position()
    leg3.initial_position()
    leg4.initial_position()
    leg5.initial_position()

    time.sleep(5)

    leg0.lower_leg()
    leg1.lower_leg()
    leg2.lower_leg()
    leg3.lower_leg()
    leg4.lower_leg()
    leg5.lower_leg()

    time.sleep(5)

    leg0.initial_position()
    leg1.initial_position()
    leg2.initial_position()
    leg3.initial_position()
    leg4.initial_position()
    leg5.initial_position()




# gammel kode:
"""
    servo = Servo(ctrl, 0, 2000, 5950) # creating servo object 2000min pos, 5950 max pos
    servo2 = Servo(ctrl, 1, 3950, 6900) # creating servo object 2000min pos, 5950 max pos
    servo3 = Servo(ctrl, 2, 4000, 7550) # creating servo object 2000min pos, 5950 max pos

    servo.move(2000)
    servo2.move(3950)
    servo3.move(4000)
    ctrl.close()

    leg0 = Leg(ctrl, 0, 0, 1, 2)
    leg0.lift_leg()

    creepy_pod = CreepyPod()
    creepy_pod.display_state()
    creepy_pod.change_state(CreepyState.IDLE)
    creepy_pod.display_state()
"""
if __name__ == "__main__":
    main()

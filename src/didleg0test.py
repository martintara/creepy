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
        Servo(ctrl, 0, 5400, 450, 0, 45),
        Servo(ctrl, 1, 6125, 3775, 0, 45),
        Servo(ctrl, 2, 4850, 3250, 0, 45)
                    ]


    servo_list1 = [
        Servo(ctrl, 3, 6025, 450, 90, 90),
        Servo(ctrl, 4, 6400, 3775, 90, 90),
        Servo(ctrl, 5, 5125, 3250, 90, 90)
                   ]

    servo_list2 = [
        Servo(ctrl, 6, 6600, 450, 90, 90),
        Servo(ctrl, 7, 6450, 3775, 90, 90),
        Servo(ctrl, 8, 5050, 3250, 90, 90)
                   ]

    servo_list3 = [
        Servo(ctrl, 9, 5350, 450, 90, 90),
        Servo(ctrl, 10, 5875, 3775, 90, 90),
        Servo(ctrl, 11, 5200, 3250, 90, 90)
            ]

    servo_list4 = [
        Servo(ctrl, 12, 5600, 450, 90, 90),
        Servo(ctrl, 13, 6400, 3775, 90, 90),
        Servo(ctrl, 14, 5025, 3250, 90, 90)
                   ]

    servo_list5 = [
        Servo(ctrl, 15, 5400, 450, 90, 90),
        Servo(ctrl, 16, 6250, 3775, 90, 90),
        Servo(ctrl, 17, 5025, 3250, 90, 90)
                   ]




    leg0 = Leg(ctrl, 0, servo_list0)
    leg1 = Leg(ctrl, 1, servo_list1)
    leg2 = Leg(ctrl, 2, servo_list2)
    leg3 = Leg(ctrl, 3, servo_list3)
    leg4 = Leg(ctrl, 4, servo_list4)
    leg5 = Leg(ctrl, 5, servo_list5)





    
    leg0.initial_position()
    leg1.initial_position()
    leg2.initial_position()
    leg3.initial_position()
    leg4.initial_position()
    leg5.initial_position()
    time.sleep(3)
    leg0.standby_position()
    leg1.standby_position()
    leg2.standby_position()
    leg3.standby_position()
    leg4.standby_position()
    leg5.standby_position()
    time.sleep(3)
    leg1.rise_leg()
    leg3.rise_leg()
    leg5.rise_leg()
    leg1.rotate_backward()
    leg3.rotate_forward()
    leg5.rotate_forward()
    time.sleep(3)
    leg1.lower_leg()
    leg3.lower_leg()
    leg5.lower_leg()
    time.sleep(3)
    leg0.rise_leg()
    leg2.rise_leg()
    leg4.rise_leg()
    leg0.rotate_backward()
    leg2.rotate_backward()
    leg4.rotate_forward()
    leg1.rotate_forward()
    leg3.rotate_backward()
    leg5.rotate_backward()
    time.sleep(3)
    leg0.lower_leg()
    leg2.lower_leg()
    leg4.lower_leg()
    time.sleep(3)
    leg0.rotate_forward()
    leg2.rotate_forward()
    leg4.rotate_backward()
    leg1.rise_leg()
    leg3.rise_leg()
    leg5.rise_leg()
    leg1.rotate_backward()
    leg3.rotate_forward()
    leg5.rotate_forward()
    time.sleep(3)
    leg1.lower_leg()
    leg3.lower_leg()
    leg5.lower_leg()
    
    val = 0

    while val < 1:
        time.sleep(3)
        leg0.rise_leg()
        leg2.rise_leg()
        leg4.rise_leg()
        leg0.rotate_backward()
        leg2.rotate_backward()
        leg4.rotate_forward()
        leg1.rotate_forward()
        leg3.rotate_backward()
        leg5.rotate_backward()
        time.sleep(3)
        leg0.lower_leg()
        leg2.lower_leg()
        leg4.lower_leg()
        time.sleep(3)
        leg0.rotate_forward()
        leg2.rotate_forward()
        leg4.rotate_backward()
        leg1.rise_leg()
        leg3.rise_leg()
        leg5.rise_leg()
        leg1.rotate_backward()
        leg3.rotate_forward()
        leg5.rotate_forward()
        time.sleep(3)
        leg1.lower_leg()
        leg3.lower_leg()
        leg5.lower_leg()
        
        val += 1
        
    leg0.initial_position()
    leg1.initial_position()
    leg2.initial_position()
    leg3.initial_position()
    leg4.initial_position()
    leg5.initial_position()
 


      






if __name__ == "__main__":
    main()

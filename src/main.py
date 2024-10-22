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
    leg1 = Leg(ctrl, 1, 3, 4, 5)
    leg1.initial_position()
    time.sleep(5)
    leg1.lower_leg()
    time.sleep(5)
    leg1.initial_position()


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

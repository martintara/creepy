# main.py

from creepy_pod import CreepyPod
from creepy_state import CreepyState
# from maestro import Controller
# import maestro

# from servo import Servo

def main():
    """ testing av servo-objekter (testet! fungerer!)
    ctrl = maestro.Controller()

    servo = Servo(ctrl, 17, 2000, 5950) # creating servo object 2000min pos, 5950 max pos
    servo2 = Servo(ctrl, 16, 3950, 6900) # creating servo object 2000min pos, 5950 max pos
    servo3 = Servo(ctrl, 15, 4000, 7550) # creating servo object 2000min pos, 5950 max pos

    servo.move(5000)
    servo2.move(5000)
    servo3.move(5000)
    ctrl.close()
    """

    creepy_pod = CreepyPod()
    creepy_pod.display_state()
    creepy_pod.change_state(CreepyState.IDLE)
    creepy_pod.display_state()

if __name__ == "__main__":
    main()

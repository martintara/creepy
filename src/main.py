# main.py

from creepy_pod import CreepyPod
from creepy_state import CreepyState
# from maestro import Controller
# import maestro
# from leg import Leg
import time

# from servo import Servo

def main():
    creepy_pod = CreepyPod()  # Initialize CreepyPod in STARTUP state

    # Run state actions until shutdown
    while creepy_pod.state != CreepyState.SHUTDOWN:
        creepy_pod.run_state_action()

    print("CreepyPod has shut down.")

if __name__ == "__main__":
    main()

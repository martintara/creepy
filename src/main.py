# main.py

from creepy_pod import CreepyPod
from creepy_state import CreepyState
from maestro import Controller
import maestro
import time

def main():
    # servo controller communication object
    ctrl = maestro.Controller()
    creepy_pod = CreepyPod(ctrl)  # Initialize CreepyPod in STARTUP state

    # Run state actions until shutdown
    while creepy_pod.state != CreepyState.EXIT:
        creepy_pod.run_state_action()

    print("CreepyPod has shut down.")

if __name__ == "__main__":
    main()
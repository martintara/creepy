# main.py hei!
import json
from creepy_pod import CreepyPod
from creepy_state import CreepyState
from maestro import Controller
import maestro
# from leg import Leg
import time

# from servo import Servo

def main():
    def load_leg_params(filename):
        """Load leg parameters from a JSON file."""
        with open(filename, 'r') as file:
            leg_params = json.load(file)
        return leg_params 
    # servo controller communication object
    ctrl = maestro.Controller()
    leg_params = load_leg_params("default_leg_params.json")
    
    creepy_pod = CreepyPod(leg_params, ctrl)  # Initialize CreepyPod in STARTUP state

    # Run state actions until shutdown
    while creepy_pod.state != CreepyState.EXIT:
        creepy_pod.run_state_action()

    print("CreepyPod has shut down.")

if __name__ == "__main__":
    main()

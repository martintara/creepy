# main.py
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
    leg_params = load_leg_params("leg_params.json")
    # Servo settings
    # leg_params = [
    #         {
    #         "offset": 315,
    #         "servos": [
    #             {"channel": 0, "center_pos": 5900, "range": 2350, "center_angle": 0, "angle_range": 45},
    #             {"channel": 1, "center_pos": 6125, "range": 3775, "center_angle": 0, "angle_range": 45},
    #             {"channel": 2, "center_pos": 5100, "range": 3000, "center_angle": 0, "angle_range": 70}
    #         ]
    #         },
    #         { 
    #         "offset": 0,
    #         "servos": [  # Leg 1
    #             {"channel": 3, "center_pos": 6025, "range": 2350, "center_angle": 90, "angle_range": 90},
    #             {"channel": 4, "center_pos": 6400, "range": 3775, "center_angle": 90, "angle_range": 90},
    #             {"channel": 5, "center_pos": 5125, "range": 3250, "center_angle": 90, "angle_range": 90}
    #         ]
    #         },
    #         { 
    #         "offset": 45,
    #         "servos": [  # Leg 2
    #             {"channel": 6, "center_pos": 6400, "range": 2350, "center_angle": 90, "angle_range": 90},
    #             {"channel": 7, "center_pos": 6450, "range": 3775, "center_angle": 90, "angle_range": 90},
    #             {"channel": 8, "center_pos": 5050, "range": 3250, "center_angle": 90, "angle_range": 90}
    #         ]
    #         },
    #         { 
    #         "offset": 135,
    #         "servos": [  # Leg 3
    #             {"channel": 9, "center_pos": 5750, "range": 2350, "center_angle": 90, "angle_range": 90},
    #             {"channel": 10, "center_pos": 5875, "range": 3775, "center_angle": 90, "angle_range": 90},
    #             {"channel": 11, "center_pos": 5200, "range": 3250, "center_angle": 90, "angle_range": 90}
    #         ]
    #         },
    #         { 
    #         "offset": 180,
    #         "servos": [  # Leg 4
    #             {"channel": 12, "center_pos": 5600, "range": 2350, "center_angle": 90, "angle_range": 90},
    #             {"channel": 13, "center_pos": 6400, "range": 3775, "center_angle": 90, "angle_range": 90},
    #             {"channel": 14, "center_pos": 5025, "range": 3250, "center_angle": 90, "angle_range": 90}
    #         ]
    #         },
    #         { 
    #         "offset": 225,
    #         "servos": [  # Leg 5
    #             {"channel": 15, "center_pos": 5000, "range": 2350, "center_angle": 90, "angle_range": 90},
    #             {"channel": 16, "center_pos": 6250, "range": 3775, "center_angle": 90, "angle_range": 90},
    #             {"channel": 17, "center_pos": 5025, "range": 3250, "center_angle": 90, "angle_range": 90}
    #         ]
    #         }
    #     ]


    creepy_pod = CreepyPod(leg_params, ctrl)  # Initialize CreepyPod in STARTUP state

    # Run state actions until shutdown
    while creepy_pod.state != CreepyState.EXIT:
        creepy_pod.run_state_action()

    print("CreepyPod has shut down.")

if __name__ == "__main__":
    main()
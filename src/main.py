# main.py

from creepy_pod import CreepyPod
from creepy_state import CreepyState
from maestro import Controller
import maestro
import time

# from servo import Servo

def main():
    # Servo controller communication object
    ctrl = maestro.Controller()

    # Defining parameters for each leg manually
    leg_params = [
        {
        "offset": 315,
        "servos": [
            {"servo_id": 0, "center_pos": 5900, "range": 2350, "center_angle": 0, "angle_range": 45},
            {"servo_id": 1, "center_pos": 6125, "range": 3775, "center_angle": 0, "angle_range": 45},
            {"servo_id": 2, "center_pos": 5100, "range": 3000, "center_angle": 0, "angle_range": 70}
        ]
        },
        { 
        "offset": 0,
        "servos": [  # Leg 1
            {"servo_id": 3, "center_pos": 6025, "range": 2350, "center_angle": 90, "angle_range": 90},
            {"servo_id": 4, "center_pos": 6400, "range": 3775, "center_angle": 90, "angle_range": 90},
            {"servo_id": 5, "center_pos": 5125, "range": 3250, "center_angle": 90, "angle_range": 90}
        ]
        },
        { 
        "offset": 45,
        "servos": [  # Leg 2
            {"servo_id": 6, "center_pos": 6400, "range": 2350, "center_angle": 90, "angle_range": 90},
            {"servo_id": 7, "center_pos": 6450, "range": 3775, "center_angle": 90, "angle_range": 90},
            {"servo_id": 8, "center_pos": 5050, "range": 3250, "center_angle": 90, "angle_range": 90}
        ]
        },
        { 
        "offset": 135,
        "servos": [  # Leg 3
            {"servo_id": 9, "center_pos": 5750, "range": 2350, "center_angle": 90, "angle_range": 90},
            {"servo_id": 10, "center_pos": 5875, "range": 3775, "center_angle": 90, "angle_range": 90},
            {"servo_id": 11, "center_pos": 5200, "range": 3250, "center_angle": 90, "angle_range": 90}
        ]
        },
        { 
        "offset": 180,
        "servos": [  # Leg 4
            {"servo_id": 12, "center_pos": 5600, "range": 2350, "center_angle": 90, "angle_range": 90},
            {"servo_id": 13, "center_pos": 6400, "range": 3775, "center_angle": 90, "angle_range": 90},
            {"servo_id": 14, "center_pos": 5025, "range": 3250, "center_angle": 90, "angle_range": 90}
        ]
        },
        { 
        "offset": 225,
        "servos": [  # Leg 5
            {"servo_id": 15, "center_pos": 5000, "range": 2350, "center_angle": 90, "angle_range": 90},
            {"servo_id": 16, "center_pos": 6250, "range": 3775, "center_angle": 90, "angle_range": 90},
            {"servo_id": 17, "center_pos": 5025, "range": 3250, "center_angle": 90, "angle_range": 90}
        ]
        }
    ]

    creepy_pod = CreepyPod(leg_params, ctrl)  # Initialize CreepyPod in STARTUP state

    # Run state actions until shutdown
    while creepy_pod.state != CreepyState.SHUTDOWN:
        creepy_pod.run_state_action()

    print("CreepyPod has shut down.")

if __name__ == "__main__":
    main()

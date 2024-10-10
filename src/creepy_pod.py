# generert på chat gpt - ikke implementert korrekt enda

# creepy_pod.py
from leg import Leg

class CreepyPod:
    def __init__(self):
        # Initialize 6 legs
        self.legs = [Leg(i) for i in range(6)]

    def move_pod(self, leg_positions: list[list[int]]):
        """
        Moves each leg's servos to the given positions.
        leg_positions should be a list of 6 sub-lists, each containing 3 positions for the servos.
        """
        if len(leg_positions) != 6:
            raise ValueError("CreepyPod must have exactly 6 legs.")
        
        for i, positions in enumerate(leg_positions):
            print(f"Moving leg {i}")
            self.legs[i].move_leg(positions)


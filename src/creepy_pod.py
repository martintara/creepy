# NB move_pod() er fortsatt noe gammelt generert fra chat gpt. se over dette
# har ikke testet dette enda
# creepy_pod.py
from creepy_state import CreepyState
#from leg import Leg

class CreepyPod:
    def __init__(self):
        self.state = CreepyState.STARTUP # Initial state
        print(f"Entering state: {self.state.name}") # notat: state.name fungerer fordi Enum har en name funksjon
        # Initialize 6 legs
 #       self.legs = [Leg(i) for i in range(6)]

    def change_state(self, new_state: CreepyState):
        print(f"Changing state from {self.state.name} to {new_state.name}")
        self.state = new_state

    def display_state(self):
        print(f"Current state: {self.state.name}")


#    def move_pod(self, leg_positions: list[list[int]]):
#        """
#        Moves each leg's servos to the given positions.
#        leg_positions should be a list of 6 sub-lists, each containing 3 positions for the servos.
#        """
#        if len(leg_positions) != 6:
#            raise ValueError("CreepyPod must have exactly 6 legs.")
#        
#        for i, positions in enumerate(leg_positions):
#            print(f"Moving leg {i}")
#            self.legs[i].move_leg(positions)


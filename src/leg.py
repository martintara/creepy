# generert på chat gpt - ikke implementert korrekt enda

# leg.py
from servo import Servo

class Leg:
    def __init__(self, leg_id: int):
        self.leg_id = leg_id  # Unique identifier for the leg
        self.servos = [Servo(i) for i in range(3)]  # Each leg has 3 servos

    def move_leg(self, positions: list[int]):
        """Moves all servos in the leg to the given positions."""
        if len(positions) != 3:
            raise ValueError("Each leg must have exactly 3 servo positions.")
        for i, pos in enumerate(positions):
            self.servos[i].move(pos)


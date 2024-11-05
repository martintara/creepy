# leg.py
from servo import Servo
from maestro import Controller

class Leg:
    def __init__(self, leg_id: int, servo_params, ctrl: Controller, offset=0):
        self.leg_id = leg_id  # Unique identifier for the leg
        self.offset = offset
        self.servos = [Servo(ctrl, **params) for params in servo_params]  # Initialize servos for the leg
    def lower_leg(self):
        self.servos[1].move_to_angle(57)

        self.servos[2].move_to_angle(40)

    def rise_leg(self):
        self.servos[1].move_to_angle(90)



    def initial_position(self):
#       self.servos[0].move(int((self.servos[0].max_pos+self.servos[0].min_pos)/2))
        self.servos[0].move(self.servos[0].center_pos)
        self.servos[1].move(self.servos[1].max_pos)
        self.servos[2].move(self.servos[2].max_pos)

    def straight_up(self):
#       self.servos[0].move(int((self.servos[0].max_pos+self.servos[0].min_pos)/2))
#       self.servos[0].move(self.servos[0].center_pos)
        self.servos[1].move(self.servos[1].max_pos)
        self.servos[2].move(self.servos[2].min_pos)

    def straight_down(self):
#       self.servos[0].move(int((self.servos[0].max_pos+self.servos[0].min_pos)/2))
        self.servos[0].move(self.servos[0].center_pos)
        self.servos[1].move(self.servos[1].min_pos)
        self.servos[2].move(self.servos[2].min_pos)

    def leg_forward(self):
        """Move leg forward, adjusted for orientation."""
        # Move to max_pos for forward if offset is in [315, 45, 225, 135]
        if self.offset in [315, 45, 0]:
            forward_position = self.servos[0].max_pos
        else:
            # Otherwise, move to min_pos for forward (center legs with offsets 0 and 180)
            forward_position = self.servos[0].min_pos

        self.servos[0].move(forward_position)
        print(f"Leg {self.leg_id} moved forward with orientation offset {self.offset}, "
              f"minpos {self.servos[0].min_pos}, maxpos {self.servos[0].max_pos}")


    def leg_backward(self):
        """Move leg backward, adjusted for orientation."""
        backward_position = self.servos[0].min_pos if self.offset in [315, 45, 0] else self.servos[0].max_pos
        self.servos[0].move(backward_position)
        print(f"Leg {self.leg_id} moved backward with orientation offset {self.offset}")

    def manual_control(self, id: int):
        self.servos[id].manual_control()

    def manual_control_angle(self, id: int):
        self.servos[id].manual_control_angle()

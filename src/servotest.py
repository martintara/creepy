import maestro
servo = maestro.Controller()
servo.setAccel(0,4)
servo.setTarget(0,3000)
x = servo.getPosition(0)
servo.close()

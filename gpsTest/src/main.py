# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       junnaaa                                                      #
# 	Created:      10/13/2024, 3:18:14 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import math as m
# Brain should be defined by default
brain=Brain()
#assigning motors
rightBack = Motor(Ports.PORT19, GearSetting.RATIO_6_1, True)
rightFront = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)
rightTop = Motor(Ports.PORT18, GearSetting.RATIO_6_1, False)
leftBack = Motor(Ports.PORT13, GearSetting.RATIO_6_1, False)
leftFront = Motor(Ports.PORT11, GearSetting.RATIO_6_1, False)
leftTop = Motor(Ports.PORT14, GearSetting.RATIO_6_1, True)
intake = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
#assigning motor groups for drivetrain and intake
rightSide = MotorGroup(rightBack, rightFront, rightTop)
leftSide = MotorGroup(leftBack, leftFront, leftTop)
#assigning non motor ports
armMotor = Motor(Ports.PORT6, GearSetting.RATIO_36_1, True)
control = Controller(PRIMARY)
slam = DigitalOut(brain.three_wire_port.a)
mogoMech = DigitalOut(brain.three_wire_port.b)
inertia = Inertial(Ports.PORT2)
gps = Gps(Ports.PORT10, 0.00, 165.10, MM, 0)
driveTrain = SmartDrive(leftSide, rightSide, gps, 299.24, 320, 40, MM, 1.3333333333333333)


def moveTo(x, y):
    o = x - gps.x_position()
    a = y - gps.y_position()
    c = m.sqrt(a**2 + o**2)
    angle = m.atan(o/a)
    if a < 0 :
        angle = 180-angle
    driveTrain.turn_to_heading(angle, DEGREES)
    driveTrain.drive_for(FORWARD, c, MM)
def auto():
    moveTo(0,0)
auto()

# Library imports
from vex import *
import math as m
# Brain should be defined by default
brain=Brain()
#Assigning ports
#assigning motors
rightBack = Motor(Ports.PORT19, GearSetting.RATIO_6_1, True)
rightFront = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)
rightTop = Motor(Ports.PORT18, GearSetting.RATIO_6_1, False)
leftBack = Motor(Ports.PORT13, GearSetting.RATIO_6_1, False)
leftFront = Motor(Ports.PORT11, GearSetting.RATIO_6_1, False)
leftTop = Motor(Ports.PORT14, GearSetting.RATIO_6_1, True)
intake = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True )
#assigning motor groups for drivetrain and intake

rightSide = MotorGroup(rightBack, rightFront, rightTop)
leftSide = MotorGroup(leftBack, leftFront, leftTop)
#assigning non motor ports
armMotor = Motor(Ports.PORT6, GearSetting.RATIO_36_1, True)
control = Controller(PRIMARY)
slam = DigitalOut(brain.three_wire_port.a)
mogoMech = DigitalOut(brain.three_wire_port.b)
inertia = Inertial(Ports.PORT2)
driveTrain = DriveTrain(leftSide, rightSide, 319.19, 295, 230, MM, 1.3333333333333333)


while True:
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print('leftFronta: '+str(leftFront.temperature(PERCENT)/2+20))
    brain.screen.next_row()
    brain.screen.print('rightFronta: '+str(rightFront.temperature(PERCENT)/2+20))
    brain.screen.next_row()
    brain.screen.print('leftBacka: '+str(leftBack.temperature(PERCENT)/2+20))
    brain.screen.next_row()
    brain.screen.print('rightbacka: '+str(rightBack.temperature(PERCENT)/2+20))
    brain.screen.next_row()
    brain.screen.print('leftTop: '+str(leftTop.temperature(PERCENT)/2+20))
    brain.screen.next_row()
    brain.screen.print('rightTop: '+str(rightTop.temperature(PERCENT)/2+20))
    brain.screen.next_row()
    brain.screen.print('intake: '+str(intake.temperature(PERCENT)/2+20))
    wait(1,SECONDS)
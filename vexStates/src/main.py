# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Paxton Bennison                                              #
# 	Created:      7/11/2024, 8:34:42 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

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
intake1 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
intake2 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True )
#assigning motor groups for drivetrain and intake
intake = MotorGroup(intake1, intake2)
rightSide = MotorGroup(rightBack, rightFront, rightTop)
leftSide = MotorGroup(leftBack, leftFront, leftTop)
#assigning non motor ports
armMotor = Motor(Ports.PORT6, GearSetting.RATIO_36_1, True)
control = Controller(PRIMARY)
slam = DigitalOut(brain.three_wire_port.a)
mogoMech = DigitalOut(brain.three_wire_port.b)
inertia = Inertial(Ports.PORT2)
driveTrain = SmartDrive(leftSide, rightSide, inertia, 299.24, 320, 40, MM, 1.3333333333333333)
#movement functions for auto


   
def sgn(x): #sign function. makes everything positive or negative one
    if x == 0:
        return 0
    return (x > 0) * 2 - 1
def preAuto():
   # Start calibration.
    inertia.calibrate()
# Print that the Inertial Sensor is calibrating while
# waiting for it to finish calibrating.
    while inertia.is_calibrating():
        control.screen.clear_screen()
        control.screen.set_cursor(1,1)
        control.screen.print("Inertial Sensor Calibrating")
        wait(50, MSEC)
    control.screen.clear_screen()
    control.screen.set_cursor(1,1)
    control.screen.print("Inertial Sensor Done")
def auto():
    leftSide.set_stopping(HOLD)
    rightSide.set_stopping(HOLD)
def driveA():
    mogoToggle = False
    canMogo = True
    slamToggle = False
    canSlam = True
    while True:
        if mogoToggle:
            mogoMech.set(True)
        else:
            mogoMech.set(False)
        if slamToggle:
            slam.set(True)
        else:
            slam.set(False)
        rightSide.set_stopping(COAST)
        leftSide.set_stopping(COAST)
        rightSide.spin(FORWARD)
        leftSide.spin(FORWARD)
        axis3 = control.axis3.position()
        axis1 = ((m.e**(-2.3+2.3*abs(control.axis1.position()/100)))*sgn(control.axis1.position()/100))*100
        leftSide.set_velocity(axis3-axis1, PERCENT)
        rightSide.set_velocity(axis3+axis1, PERCENT)
        intake.spin(FORWARD)
        armMotor.spin(FORWARD)
        if control.buttonA.pressing() and canMogo:
            canMogo = False
            if not mogoToggle:
                mogoToggle = True
            elif mogoToggle:
                mogoToggle = False
        elif not control.buttonA.pressing():
            canMogo = True
        if control.buttonB.pressing() and canSlam:
            canSlam = False
            if not slamToggle:
                slamToggle = True
            elif slamToggle:
                slamToggle = False
        elif not control.buttonB.pressing():
            canSlam = True     
        if control.buttonR1.pressing():
            intake.set_velocity(100, PERCENT)
        elif control.buttonR2.pressing():
            intake.set_velocity(-100, PERCENT)
        else:
            intake.stop()
        if control.buttonL1.pressing():
            armMotor.set_velocity(100, PERCENT)
        elif control.buttonL2.pressing():
            armMotor.set_velocity(-100, PERCENT)
        else:
            armMotor.set_velocity(0)
def inertial():
    global multi, difference
    a = 0
    while True:
        control.screen.set_cursor(1,1)
        brain.screen.set_cursor(1,1)
        control.screen.print("inertial heading: " + str(round(inertia.heading(), 2)))
        control.screen.new_line()
        if comp.is_autonomous():
            #a += 1
            #control.screen.print(multi)
            #control.screen.new_line()
            #control.screen.print(str(round(difference, 1)))
            #control.screen.new_line()
            #control.screen.print(a)
            pass
        wait(0.1, SECONDS)
        control.screen.clear_screen()
        brain.screen.clear_screen
def drive():
    dTaskA = Thread( driveA )
    while( comp.is_driver_control() and comp.is_enabled()):
        wait(10, MSEC)
    dTaskA.stop()
thread = Thread(inertial)
comp = Competition(drive, auto)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
preAuto()
        

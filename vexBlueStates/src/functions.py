from vex import *
brain=Brain()
rightBack = Motor(Ports.PORT19, GearSetting.RATIO_6_1, True)
rightFront = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)
rightTop = Motor(Ports.PORT18, GearSetting.RATIO_6_1, False)
leftBack = Motor(Ports.PORT13, GearSetting.RATIO_6_1, False)
leftFront = Motor(Ports.PORT11, GearSetting.RATIO_6_1, False)
leftTop = Motor(Ports.PORT14, GearSetting.RATIO_6_1, True)
intake1 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
intake2 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True )
intake = MotorGroup(intake1, intake2)
rightSide = MotorGroup(rightBack, rightFront, rightTop)
leftSide = MotorGroup(leftBack, leftFront, leftTop)
armMotor = Motor(Ports.PORT6, GearSetting.RATIO_36_1, True)
control = Controller(PRIMARY)
slam = DigitalOut(brain.three_wire_port.a)
mogoMech = DigitalOut(brain.three_wire_port.b)
inertia = Inertial(Ports.PORT2)
#all auto functions 
def example():
    pass
def inertialTurn(position):
    inertia.reset_heading()
    if position > 0:
        difference = position
        leftSide.spin(REVERSE)
        rightSide.spin(FORWARD)
        while difference > 0.1:
            difference = position - inertia.heading()
            multi = (difference/position)*100
            leftSide.set_velocity(multi, PERCENT)
            rightSide.set_velocity(multi, PERCENT)
    else:
        difference = position
        leftSide.spin(FORWARD)
        rightSide.spin(REVERSE)
        while difference > 0.1:
            newHeading = 360-inertia.heading()
            difference = position - newHeading
            multi = (difference/position)*100
            leftSide.set_velocity(multi, PERCENT)
            rightSide.set_velocity(multi, PERCENT)
def moveForward(amount, speed, timeOut = None):
    if not timeOut == None:
        leftSide.set_timeout(timeOut, SECONDS)
        rightSide.set_timeout(timeOut, SECONDS)
    leftSide.set_velocity(speed, PERCENT)
    rightSide.set_velocity(speed, PERCENT)
    leftSide.spin_for(FORWARD, amount, TURNS, wait=False)
    rightSide.spin_for(FORWARD, amount, TURNS)
    leftSide.set_timeout(60, SECONDS)
    rightSide.set_timeout(60, SECONDS)
def moveBackward(amount, speed, timeOut = None):
    if not timeOut == None:
        leftSide.set_timeout(timeOut, SECONDS)
        rightSide.set_timeout(timeOut, SECONDS)
    leftSide.set_velocity(speed, PERCENT)
    rightSide.set_velocity(speed, PERCENT)
    leftSide.spin_for(REVERSE, amount, TURNS, wait=False)
    rightSide.spin_for(REVERSE, amount, TURNS)
    leftSide.set_timeout(60, SECONDS)
    rightSide.set_timeout(60, SECONDS)
def turnLeft(amount, speed, timeOut = None):
    if not timeOut == None:
        leftSide.set_timeout(timeOut, SECONDS)
        rightSide.set_timeout(timeOut, SECONDS)
    leftSide.set_velocity(speed, PERCENT)
    rightSide.set_velocity(speed, PERCENT)
    leftSide.spin_for(FORWARD, amount, TURNS, wait=False)
    rightSide.spin_for(REVERSE, amount, TURNS)
    leftSide.set_timeout(60, SECONDS)
    rightSide.set_timeout(60, SECONDS)
def turnRight(amount, speed, timeOut = None):
    if not timeOut == None:
        leftSide.set_timeout(timeOut, SECONDS)
        rightSide.set_timeout(timeOut, SECONDS)
    leftSide.set_velocity(speed, PERCENT)
    rightSide.set_velocity(speed, PERCENT)
    leftSide.spin_for(REVERSE, amount, TURNS, wait=False)
    rightSide.spin_for(FORWARD, amount, TURNS)
    leftSide.set_timeout(60, SECONDS)
    rightSide.set_timeout(60, SECONDS)
import turtle, math
#-------------------------------------------------------------------
#Variables that can be changed
q = 1.6 * (10**-19)  #charge of particle
QA = 0.2 * (10**-9)  #charge of first sphere
QB = -0.2 * (10**-8)  #charge of second sphere
radius = 0.03        #radius of spheres
sphereAVect = [0,0]    #position vector of sphere A
sphereBVect = [0.2,0]  #position vector of sphere B
particleMass = 1.67 * (10 ** -27)
angle = 100
#-------------------------------------------------------------------

particleVelocity = [[0,0],[0,0]] #[0] for A [1] for B
particleAcceleration = [0, 0]
particleDisplacement =[radius*math.cos((angle/360)*2*math.pi), radius*math.sin((angle/360)*2*math.pi)]
elecConst = 8.85418782*(10**-12)
time = 0
timeDiff = 1 * (10**-8)
run = True


def findDistance(vectA,vectB):
    resultant = [vectA[0]-vectB[0],vectA[1]-vectB[1]]
    distance = math.sqrt((resultant[0])**2+(resultant[1])**2)
    return distance


def getForce(AorB):
    if AorB:
        vectDirection = [particleDisplacement[0] - sphereAVect[0], particleDisplacement[1] - sphereAVect[1]]
        vectmag = math.sqrt((vectDirection[0])**2+(vectDirection[1])**2)
        Qq = q * QA
        denom = 4 * math.pi * elecConst * (findDistance(particleDisplacement, sphereAVect)) ** 2
        force = float(Qq / denom)
        multiplier = float(force/vectmag)
        forceVect = [vectDirection[0]*multiplier,vectDirection[1]*multiplier]
        return forceVect
    else:
        vectDirection = [particleDisplacement[0] - sphereBVect[0], particleDisplacement[1] - sphereBVect[1]]
        vectmag = math.sqrt((vectDirection[0]) ** 2 + (vectDirection[1]) ** 2)
        Qq = q * QB
        denom = 4 * math.pi * elecConst * (findDistance(particleDisplacement, sphereBVect)) ** 2
        force = float(Qq / denom)
        multiplier = float(force / vectmag)
        forceVect = [vectDirection[0] * multiplier, vectDirection[1] * multiplier]
        return forceVect


def getAcceleration(forceVect):
    force = forceVect
    acceleration = [float(force[0] / particleMass), float(force[1] / particleMass)]
    return acceleration


def getcompDisplacement(acceleration, velocity):
    S = [(velocity[0]*timeDiff)+(0.5)*(acceleration[0])*(timeDiff**2), (velocity[1]*timeDiff)+(0.5)*(acceleration[1])*(timeDiff**2)]
    return S


def getVelocity(acceleration, a):
    if a:
        return [particleVelocity[0][0]+(acceleration[0]*timeDiff),particleVelocity[0][1]+(acceleration[1]*timeDiff)]
    else:
        return [particleVelocity[1][0] + (acceleration[0] * timeDiff),particleVelocity[1][1] + (acceleration[1] * timeDiff)]

turtle.getscreen()
turtle.hideturtle()
pen = turtle.Turtle()
pen.speed(1000)
pen.hideturtle()
timestamp = turtle.Turtle()
timestamp.hideturtle()
timestamp.penup()
timestamp.sety(350)
timestamp.setx(-450)
timestamp.setx(-451)
xdispstamp = turtle.Turtle()
xdispstamp.hideturtle()
xdispstamp.penup()
xdispstamp.sety(290)
xdispstamp.setx(-450)
xdispstamp.setx(-451)
ydispstamp = turtle.Turtle()
ydispstamp.hideturtle()
ydispstamp.penup()
ydispstamp.sety(320)
ydispstamp.setx(-450)
ydispstamp.setx(-451)
angleStamp = turtle.Turtle()
angleStamp.hideturtle()
angleStamp.penup()
angleStamp.sety(-80)
angleStamp.setx(-220)
angleStamp.write("Starting angle on Sphere A: "+str(angle)+"°")
particleQ = turtle.Turtle()
particleQ.hideturtle()
particleQ.penup()
particleQ.sety(260)
particleQ.setx(-450)
particleQ.write("Particle charge: "+str(q)+" C", font=("Arial", 16, "normal"))
chargeA = turtle.Turtle();
chargeA.hideturtle()
chargeA.penup()
chargeB = turtle.Turtle();
chargeB.hideturtle()
chargeB.penup()
chargeA.goto(-230,-50)
chargeA.write(str(QA)+" C", font=("Arial", 10, "normal"))
chargeB.goto(sphereBVect[0]*1000-230,-50)
chargeB.write(str(QB)+" C", font=("Arial", 10, "normal"))
pen.penup()
pen.sety(-radius*1000)
pen.setx(-200)
pen.pendown()
pen.circle(radius*1000)
pen.penup()
pen.setx(sphereBVect[0]*1000-200)
pen.pendown()
pen.circle(radius*1000)
pen.penup()
pen.sety(particleDisplacement[1]*1000)
pen.setx(particleDisplacement[0]*1000-200)
pen.color("red")
pen.pendown()
pen.shape("circle")
pen.shapesize(0.2)
pen.showturtle()


while run:
    if(findDistance(sphereAVect, particleDisplacement)+0.001<radius or findDistance(sphereBVect, particleDisplacement)+0.001<radius):
        break
    forceA = getForce(True)
    forceB = getForce(False)
    accelA = getAcceleration(forceA)
    accelB = getAcceleration(forceB)
    veloA = getVelocity(accelA, True)
    veloB = getVelocity(accelB, False)
    particleVelocity[0][0] = veloA[0]
    particleVelocity[0][1] = veloA[1]
    particleVelocity[1][0] = veloB[0]
    particleVelocity[1][1] = veloB[1]
    displA = getcompDisplacement(accelA, veloA)
    displB = getcompDisplacement(accelB, veloB)
    sumDisplacement = [displA[0]+displB[0], displA[1]+displB[1]]
    particleDisplacement = [particleDisplacement[0] + sumDisplacement[0], particleDisplacement[1] + sumDisplacement[1]]
    pen.goto(particleDisplacement[0] * 1000-200, particleDisplacement[1] * 1000)
    timestamp.undo()
    timestamp.write("Time: "+str(time)+" seconds",font=("Arial", 16, "normal"))
    xdispstamp.undo()
    xdispstamp.write("X Displacement: " + str(round(particleDisplacement[0], 3)) + " meters", font=("Arial", 16, "normal"))
    ydispstamp.undo()
    ydispstamp.write("Y Displacement: " + str(round(particleDisplacement[1], 3)) + " meters", font=("Arial", 16, "normal"))
    time+= timeDiff

turtle.Screen().exitonclick()

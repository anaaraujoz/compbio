import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
import matplotlib.animation as animation

aix = 72
Ai = 36
ki = 1
bi = 2
aiy = 1
Bi = 0
params = [aix, Ai, ki, bi, aiy, Bi]

y0 = [7,-10]
t = np.linspace(0, 300, num=100)

def simNonInteractive(variables, t, params, ):

    X = variables[0]
    Y = variables[1]
    
    aix = params[0]
    Ai = params[1]
    ki = params[2]
    bi = params[3]
    aiy = params[4]
    Bi = params[5]

    
    Xt = (aix/(Ai + (ki * Y))) - bi
    Yt = (aiy * X) - Bi 

    return ([Xt, Yt])

y00 = [0, 0, 0, 0]

def simInteractive(variables, t):
    X1 = variables[0]
    X2 = variables[1]
    Y1 = variables[2]
    Y2 = variables[3]

    a1x = 360
    A1 = 36
    b1 = 10
    k11 = 1
    k12 = 0
    a1y = 0.5
    B1 = 0
    a2x = 360
    A2 = 43
    b2 = 10
    k21 = 0
    k22 = 1
    a2y = 0
    B2 = 0


    rX1 = (a1x * (A1 + (k11 * Y1) + (k12 * Y2))) - b1
    rX2 = (a2x * (A2 + (k21 * Y1) + (k22 * Y2))) - b2
    rY1 = (a1y * X1) - B1
    rY2 = (a2y * X2) - B2

    return([rX1, rX2, rY1, rY2])

yNonInteractive = odeint(simNonInteractive, y0, t, args=(params,))

yInteractive = odeint(simInteractive, y00, t, args=(), full_output=1)


fig, (ax1, ax2) = plt.subplots(2)

# Non Interactive 
line1 = ax1.plot(t, yNonInteractive[:,0], color="r", label="rate of mRNA transcription")
line2 = ax1.plot(t, yNonInteractive[:,1], color="b", label="rate of protein production")

ax1.legend()

line3 = ax2.plot(t, yInteractive[:,0], color="r", label="X1")
line4 = ax2.plot(t, yInteractive[:,1], color="b", label="X2")
line5 = ax2.plot(t, yInteractive[:,2], color="g", label="Y1")
line6 = ax2.plot(t, yInteractive[:,3], color="b", label="Y2")

ax2.legend()

plt.show()
import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
import matplotlib.animation as animation

# TODO make sliders for all the parameters
# TODO steady state solver
# TODO remember to update the steady state
aix = 72
Ai = 10
ki = 1 # most import slider
bi = 2
aiy = 1
Bi = 1
params = [aix, Ai, ki, bi, aiy, Bi]

y0 = [2,2]
t = np.linspace(0, 100, num=200)


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

    # both k12 and k22 must be >0 for the model to be interactive
    a1x = 360
    A1 = 36
    b1 = 10
    k11 = 1
    k12 = 0.1
    a1y = 0.5
    B1 = 0
    a2x = 360
    A2 = 43
    b2 = 10
    k21 = 0.1
    k22 = 1
    a2y = 0
    B2 = 0


    rX1 = (a1x * (A1 + (k11 * Y1) + (k12 * Y2))) - b1
    rX2 = (a2x * (A2 + (k21 * Y1) + (k22 * Y2))) - b2
    rY1 = (a1y * X1) - B1
    rY2 = (a2y * X2) - B2

    return([rX1, rX2, rY1, rY2])

# TODO figure out how to bound the function to be always f>0.
yNonInteractive = odeint(simNonInteractive, y0, t, args=(params,))

#yInteractive = odeint(simInteractive, y00, t, args=(), full_output=1)

# Make plot X(t) x Y(t)
fig, (ax1, ax2) = plt.subplots(2)

# Non Interactive 
# TODO plot steady state line reference
line1 = ax1.plot(t, yNonInteractive[:,0], color="r", label="rate of mRNA transcription")
line2 = ax1.plot(t, yNonInteractive[:,1], color="b", label="rate of protein production")

# TODO make line3 color update over time, gradient
line3 = ax2.plot(yNonInteractive[:,0], yNonInteractive[:,1], color="b", label="rateX by rateY")

ax1.legend()
ax2.legend()

plt.show()
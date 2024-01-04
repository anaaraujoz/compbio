import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint

## modelling the central dogma as ODEs
# have an initial condition
# define time
y0 = [0,0]
t = np.linspace(0,200, num=100)

## transcription = km - gammam * m
k_m = 0.2
gamma_m = 0.01
m = 1
# play with the balance between the rates k and gamma!

## translation = kp * m - gammap * p
k_p = 0.4
gamma_p = 0.05

params = [k_m, gamma_m, k_p, gamma_p]

# variables: array of two values, v = [m, p]
# t: time ??
# params: array of parameters for the equations of transcription and translation
# returns array [rate of transcription, rate of translation]
def simulation(variables, t, params):
    # is it best to have the variables in the arrays and put them on variables back inside?
    m = variables[0]
    p = variables[1]

    k_m = params[0]
    gamma_m = params[1]
    k_p = params[2]
    gamma_p = params[3]

    dmdt = k_m - (gamma_m * m)
    dpdt = (k_p * m) - (gamma_p * p)

    return([dmdt, dpdt])

# using odeint
y = odeint(sim, y0, t, args=(params,))

# plotting results
f,ax = plt.subplots(1)

line1 = ax.plot(t,y[:,0], color="b", label="M")
line2 = ax.plot(t,y[:,1], color="r", label="P")

ax.set_ylabel("Abundance")
ax.set_xlabel("Time")

ax.legend(handles=[line1, line2])

plt.show()
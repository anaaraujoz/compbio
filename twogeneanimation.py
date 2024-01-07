import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
import geneclass
from random import random
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

#mpl.use('tkagg')
# initial condition and time steps setup
y0 = [0, 0]
t = np.linspace(0, 150, num=75)

# for G1
g1 = geneclass.Gene(0.5, 0.1)
g2 = geneclass.ActivatedGene(0.5, 0.05, 5, 5)

params = [g1, g2]

def sim(variables, t, g1, g2):
    G1 = variables[0]
    G2 = variables[1]

    k1 = g1.getk()
    g1 = g1.getgamma()
    dG1dt = k1 - g1 * G1

    n = g2.getn()
    c = g2.getc()
    hill = pow(G1, n) / (pow(c, n) + pow(G1, n)) 
    dG2dt = (hill * g2.getk() ) - (g2.getgamma() * G2)

    return ([dG1dt, dG2dt])

yvec = odeint(sim, y0, t, args=(g1, g2,))


fig, ax = plt.subplots(1)

line1, = ax.plot(t, yvec[:,0], color="b", label="G1")
line2, = ax.plot(t, yvec[:,1], color="r", label="G2")

ax.set_xlabel = 'Quantity'
ax.set_ylabel = 'Time'

ax.legend(handles=[line1, line2])

#plt.show()

def update(frame):
    # adapted from matplotlib documentation

    # for each frame, update the data stored on each artist.
    # update line 1

    line1.set_xdata(t[:frame])
    y1 = yvec[:,0] # gets first column from odeint solution
    line1.set_ydata(y1[:frame]) # updates from first col

    # update line 2
    line2.set_xdata(t[:frame])
    y2 = yvec[:,1]
    line2.set_ydata(y2[:frame]) # updates from second col

    return (line1, line2)


ani = animation.FuncAnimation(fig=fig, func=update, frames=75, interval=50)
ani.save(filename="/home/anaaraujoz/compbio/twogene.gif", writer="pillow")
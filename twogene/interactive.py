import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
import matplotlib.animation as plta
import geneclass
from matplotlib.widgets import Slider
import PySide6

# initial setup
y0 = [0, 0]
t = np.linspace(0, 150, num=75)

# for G1
g1 = geneclass.Gene(0.8, 0.1)
g2 = geneclass.AffectedGene(0.5, 0.05, 5, 5)

params = [g1, g2]

def simActivation(variables, t, g1, g2):
    G1 = variables[0]
    G2 = variables[1]

    k1 = g1.getk()
    g1 = g1.getgamma()
    dG1dt = k1 - g1 * G1

    n = g2.getn()
    c = g2.getc()
    # TODO: swap next line with Gene.hillActivation()
    hill = pow(G1, n) / (pow(c, n) + pow(G1, n)) 
    # TODO: put g2.getvariable() in separate variables first
    dG2dt = (hill * g2.getk() ) - (g2.getgamma() * G2)

    return ([dG1dt, dG2dt])

def simRepression(variables, t, g1, g2):
    G1 = variables[0]
    G2 = variables[1]

    
    k1 = g1.getk()
    g1 = g1.getgamma()
    dG1dt = k1 - g1 * G1

    #n = g2.getn()
    #c = g2.getc()
    # hill = pow(c, n)/ (pow(c,n) + pow(G1, n))
    hill = float(g2.HillRepression(G1))
    k2 = g2.getk()
    g2 = g2.getgamma()
    dG2dt = (hill * k2) - (g2 * G2)


    return ([dG1dt, dG2dt])

# ODE solver for simulation function
yvec = odeint(simRepression, y0, t, args=(g1, g2,))

# defines figure and lines
fig, ax = plt.subplots(1)

line1, = ax.plot(t, yvec[:,0], color="b", label="G1")
line2, = ax.plot(t, yvec[:,1], color="r", label="G2")

# defines labels
ax.set_xlabel = 'Quantity'
ax.set_ylabel = 'Time'

ax.legend(handles=[line1, line2])

#adjust the figure to have more space
fig.subplots_adjust(left=0.25, bottom=0.5)

# rect=[leftpos, bottompos, width, height]
ax_slider_k1 = fig.add_axes(rect=[0.25, 0.1, 0.65, 0.03])
ax_slider_gamma1 = fig.add_axes(rect=[0.25, 0.2, 0.65, 0.03])

# slider has ax, label, valmin, valmax, valinit
k1slider = Slider(
    ax_slider_k1,
    label='G1 production',
    valmin=0.1,
    valmax=1, 
    valinit=g1.getk()
    )

gamma1slider = Slider(
    ax_slider_gamma1,
    label='G1 decay',
    valmin=0.1,
    valmax=1,
    valinit=g1.getgamma()
)

# update caller for k1
def updatek1(val):
    # update gene object
    g1.updateK(val)
    update(val)

# update caller for gamma1
def updateg1(val):
    g1.updateGamma(val)
    update(val)

# universal simulation function updater
def update(val):
    yvec = odeint(simRepression, y0, t, args=(g1, g2,))
    
     # gets first column from odeint solution
    line1.set_ydata(yvec[:,0]) # updates from first col
    line2.set_ydata(yvec[:,1])
    fig.canvas.draw_idle()

# register the update function with each slider
k1slider.on_changed(updatek1)
gamma1slider.on_changed(updateg1)

plt.show()
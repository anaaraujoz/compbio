import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
import geneclass
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
import PySide6
from matplotlib.offsetbox import (AnchoredOffsetbox, TextArea)
import matplotlib.colors as mplc
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
#from colorspacious import cspace_converter

# TODO sliders for initial y0
y0 = [0,0,0]
t = np.linspace(0, 200, num=100)

# setup genes
# n < 1 negative binding, n = 1 independent, n > 1 positive binding, usually caps at 4
n_coef = 9
c_coef = 1

g1 = geneclass.AffectedGene(0.5, 0.1, c_coef, n_coef)
g2 = geneclass.AffectedGene(0.5, 0.1, c_coef, n_coef)
g3 = geneclass.AffectedGene(0.5, 0.1, c_coef, n_coef)


def sim(var, t, g1, g2, g3):
    G1 = var[0]
    G2 = var[1]
    G3 = var[2]

# for G1
    c = g1.getc()
    n = g1.getn()

    #hill1 = (c**n)/((c**n) + (G3**n))
    hill1 = g1.HillRepression(G3)
    k1 = g1.getk()
    gam1 = g1.getgamma()
    dG1 = (hill1 * k1) - (gam1 * G1)

# for G2
    hill2 = g2.HillActivation(G1)
    hill2 = (G1**n)/(c**n + G1**n)
    dG2 = (hill2 * g2.getk()) - (g2.getgamma() * G2)

# for G3
    hill3 = g3.HillActivation(G2)
    #hill3 = (G2**n)/(c**n + G2**n)
    dG3 = (hill3 * g3.getk()) - (g3.getgamma() * G3)

    return ([dG1, dG2, dG3])

yvec = odeint(sim, y0, t, args=(g1, g2, g3, ))

fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False)


#frame_text = ax4.text(5,5, "n coefficient")
line1 = ax1.plot(t, yvec[:,0], color="b", label="Gene 1", alpha=0)
line2 = ax2.plot(t, yvec[:,1], color="r", label="Gene 2", alpha=0)
line3 = ax3.plot(t, yvec[:,2], color="g", label="Gene 3", alpha=0)

#ax1.set_xlabel = 'Quantity'
#ax1.set_ylabel = 'Time'

ax1.legend()
ax2.legend()
ax3.legend()

steps = np.linspace(0, 4, num=75)
def update(frame):
    ax1.clear()
    ax2.clear()
    ax3.clear()
    
    # update n coefficient according to frame
    g1.updateN(frame)
    g2.updateN(frame)
    g3.updateN(frame)
    
    # update ode solver
    yvec = odeint(sim, y0, t, args=(g1, g2, g3, ))
    line1 = ax1.plot(t, yvec[:,0], color="b", label="Gene 1")
    line2 = ax2.plot(t, yvec[:,1], color="r", label="Gene 2")
    line3 = ax3.plot(t, yvec[:,2], color="g", label="Gene 3")


    ax1.legend()
    ax2.legend()
    ax3.legend()
        
    box = TextArea('Hill coefficient: %5.3f' % frame, textprops=dict(color="k"))
    
    anchored_box = AnchoredOffsetbox(loc='upper left',
                                 child=box,
                                 frameon=True,
                                 bbox_to_anchor=(0., 1.4),
                                 bbox_transform=ax1.transAxes,
                                 borderpad=0.,)
    ax1.add_artist(anchored_box)
    plt.subplots_adjust(hspace=0.5)
    
    return (line1, line2, line3)

colmap = mpl.colormaps['viridis_r']
cmapped = mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(0, 4), cmap=colmap)

def updateRainbow(frame):

    # update n coefficient according to frame
    g1.updateN(frame)
    g2.updateN(frame)
    g3.updateN(frame)
    
    # get color by frame
    new_color = cmapped.to_rgba(frame) 

    # update ode solver
    yvec = odeint(sim, y0, t, args=(g1, g2, g3, ))
    line1 = ax1.plot(t, yvec[:,0], color=new_color, label="Gene 1")
    line2 = ax2.plot(t, yvec[:,1], color=new_color, label="Gene 2")
    line3 = ax3.plot(t, yvec[:,2], color=new_color, label="Gene 3")

        
    box = TextArea('Hill coefficient: %5.3f' % frame, textprops=dict(color="k"))
    
    anchored_box = AnchoredOffsetbox(loc='upper left',
                                 child=box,
                                 frameon=True,
                                 bbox_to_anchor=(0., 1.4),
                                 bbox_transform=ax1.transAxes,
                                 borderpad=0.,)
    ax1.add_artist(anchored_box)

    plt.subplots_adjust(bottom=0.2, right=0.8, top=0.9)


    return (line1, line2, line3)

axins = inset_axes(ax3,
                    width="100%",  
                    height="10%",
                    loc='lower center',
                    borderpad=-3
                   )

# color bar
fig.colorbar(cmapped, cmap=colmap, pad=0.2,
             cax=axins, orientation='horizontal', label='Hill coefficient')


ani = animation.FuncAnimation(fig=fig, func=updateRainbow, frames=steps, interval=50,
                              repeat=False)
ani.save(filename="/home/anaaraujoz/compbio/oscnetwork/3geneanimation0-4.gif", writer="pillow")
#plt.show()
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider
import PySide6
matplotlib.use('QtAgg')

amp = 1.0
f = 1.0

fig, ax = plt.subplots()

t = np.linspace(0, (2 * np.pi), num=100)
s = amp * np.sin(f * t)
l, = ax.plot(t, s, lw=2)

ax_slider = plt.axes(arg=[0.25, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, label='Frequency', valmin=0.1, valmax=5.0)


def update(val):
    f = slider.val
    l.set_ydata(amp * np.sin(f * t))
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()
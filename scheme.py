import matplotlib
import schemdraw
import schemdraw.elements as elm

matplotlib.rcParams['svg.fonttype'] = 'none'

with schemdraw.Drawing() as d:
    d.add(elm.Resistor())
    d.add(elm.Capacitor())
    d.add(elm.Diode())
d.draw()

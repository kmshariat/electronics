#importing schemdraw module for circuit designing purposes
#current division

import schemdraw
import schemdraw.elements as elm


with schemdraw.Drawing() as d:
    d.config(inches_per_unit=.5, unit=3, color = 'yellow')
    d += (A := elm.Dot().label('A'))
    d += (node1 := elm.Line().right(d.unit/2).dot())
    d += elm.Resistor().right().label('$2a \Omega$')
    d += elm.Line().up(d.unit/2).at(node1.end)
    d += elm.Resistor().right().label('$a \Omega$')
    d += elm.Line().down(d.unit/2).dot()
    d += elm.Line().right(d.unit/2)
    d += (B := elm.Dot().label('B'))
    d += elm.Line().down(d.unit/2).at(node1.end) 
    d += elm.Resistor().right().label('$3a \Omega$')
    d += elm.Line().up(d.unit/2)

    #save
    d.save('currentDivision.svg')

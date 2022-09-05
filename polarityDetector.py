#importing schemdraw module to draw circuits and labeling them
import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config(inches_per_unit=.5, unit=3)

    d += (D1 := elm.LED().color('red').up()).label('Red') #red diode
    d += (pnt := elm.Line().right(d.unit/2).dot())
    d += elm.Line().right(d.unit/2)
    d += (D2 := elm.LED().color('green').down()).label('Green') #green diode
    d += (pnt2 := elm.Line().left(d.unit/2).dot())
    d += elm.Line().left(d.unit/2)
 
    d += elm.Ground().right().at(pnt2.end) #connecting the ground

    d += elm.Resistor().up().at(pnt.end).label('$350 \Omega$')
    d += elm.Dot().label('9V') #input voltage

    d.save('polarityDetector.svg')

#Clamper Circuit
#The value of Tau = 2 sec here
#The value of the C was fixed and From tau = RC the value of R was calculated

import schemdraw
import schemdraw.elements as elm


with schemdraw.Drawing() as d:
    d.config(inches_per_unit=.5, unit=3)
    d += (A := elm.Dot())
    d += elm.Capacitor2().dot().label('10 $\mu$F')
    d += (node1:= elm.Line().right(d.unit/2))
    d += elm.Resistor().down().label('200 k $\Omega$', loc='bottom')
    d += elm.Line().right(d.unit/2).at(node1.end)
    d += elm.Dot().label('+', loc='right')

    d += (node2 := elm.SourceSin().at(A.end).down().label('$2 V $'))
    d += elm.Ground()
    d += (node3 := elm.Line().at(node2.end).right().dot())
    d += elm.Diode(fill=True).up().label('$0.7 V$')
    d += elm.Line().at(node3.end).right()
    d += elm.Dot().label('-', loc='right')

    d.save('clamperCircuit.png')

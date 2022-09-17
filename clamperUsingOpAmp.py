import schemdraw
import schemdraw.elements as elm

#Clamper Circuit using Op-Amp
#active clamping has been done using this circuit
#The value of Tau = 2 sec here
#The value of the C was fixed and From tau = RC the value of R was calculated

with schemdraw.Drawing() as d:
    d.config(inches_per_unit=.5, unit=3)
    d += (Q := elm.Opamp())
    d += elm.Line().left(d.unit/2).at(Q.in2)
    d += elm.Line().down(d.unit/2)
    d += elm.Ground()

    d += elm.Line().left(d.unit/2).at(Q.in1)
    d += (node1 := elm.Resistor().up(d.unit*0.75).label('10 k $\Omega$', loc='bottom'))
    d += elm.Capacitor().left().label('10 $\mu$F')
    d += elm.SourceSin().down()
    d += elm.Ground()

    d += (node2 := elm.Line().right(d.unit*2.25).at(node1.end))
    d += elm.Line().right(d.unit/2).dot()

    d += elm.Line().right(d.unit/2).at(Q.out)
    d += elm.Diode(fill = True).up(d.unit*0.95).label('0.7 V')

    d += elm.Resistor().down().at(node2.end).label('200 k $\Omega$', loc='bottom')
    d += elm.Ground()

    d.save('clamperUsingOpAmp.png')

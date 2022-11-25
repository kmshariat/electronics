import schemdraw
import schemdraw.elements as elm


with schemdraw.Drawing() as d:
    d.config(inches_per_unit=.5, unit=3)

    d += (Amp := elm.Opamp(leads=True))

    d += elm.Resistor().left().at(Amp.in1).label('$R_i$')
    d += elm.Line().down(d.unit*2)
    d += elm.Line().right(d.unit*5.62)

    d += (C1 := elm.Capacitor2().label('$C$').at(Amp.out))
    d += (C2 := elm.Capacitor2().label('$C$'))
    d += (C3 := elm.Capacitor2().label('$C$'))
    d += elm.Line().right(d.unit/2)
    d += elm.Line().down(d.unit*1.8)

    d += elm.Resistor().down().at(C1.end).label('$R$')
    d += elm.Ground()
    d += elm.Resistor().down().at(C2.end).label('$R$')
    d += elm.Ground()
    d += elm.Resistor().down().at(C3.end).label('$R$')
    d += elm.Ground()

    d += elm.Ground().at(Amp.in2)

    d += elm.Line().up(d.unit*0.75).at(Amp.in1)
    d += elm.Resistor().right(d.unit*1.25).label('$R_f$')
    d += elm.Line().down(d.unit*0.95)

    d.save('phaseShiftOscillator.svg')

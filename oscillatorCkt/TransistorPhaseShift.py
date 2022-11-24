import schemdraw
import schemdraw.elements as elm


with schemdraw.Drawing() as d:
    d.config(inches_per_unit=.5, unit=3)

    d += (T := elm.BjtNpn(circle='true').anchor('collector').color('red'))
    d += elm.Resistor().up().at(T.collector).label('$R_C$', loc='bottom')
    d += (VCC := elm.Line().left(d.unit/2).dot())
    d += elm.Line().left(d.unit/2)
    d += (TE := elm.Resistor().down(d.unit*1.235)).dot().label('$R_1$', loc='bottom')
    d += elm.Resistor().down(d.unit*1.25).label('$R_2$', loc='bottom')
    d += elm.Line().right(d.unit/2).dot()
    d += elm.Ground()
    d += elm.Line().right(d.unit/2)
    d += elm.Resistor().up().label('$R_E$', loc='bottom')
    d += elm.Line().right(d.unit/2)
    d += elm.Capacitor2().down().label('$C_E$', loc='bottom')
    d += elm.Line().left(d.unit/2)

    d += elm.Line().up(d.unit/2).dot().at(VCC.end).label('$+V_{cc}$', loc='right')
    d += elm.Line().right(d.unit*0.75).at(TE.end)

    d += elm.Line().right().at(T.collector)
    d += elm.Line().down(d.unit*2)
    d += (C1 := elm.Capacitor2().left(d.unit*0.65)).label('$C$', loc='bottom')
    d += (C2 := elm.Capacitor2().left(d.unit*0.65)).label('$C$', loc='bottom')
    d += (C3 := elm.Capacitor2().left(d.unit*0.65)).label('$C$', loc='bottom')
    d += elm.Resistor().left(d.unit*0.75).label('$R^,$', loc='bottom')
    d += elm.Line().up(d.unit*1.77)
    d += elm.Line().right(d.unit*0.65)

    d += elm.Resistor().at(C1.end).down(d.unit*0.65).label('$R$', loc='bottom')
    d += elm.Ground()
    d += elm.Resistor().at(C2.end).down(d.unit*0.65).label('$R$', loc='bottom')
    d += elm.Ground()

    d.save('TransistorPhaseShiftOscillator.svg')

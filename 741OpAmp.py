import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config(inches_per_unit=.5, unit=3)
    d += (Q1 := elm.Opamp(leads='True'))
    d += elm.Line().left(d.unit*0.5).at(Q1.in2)
    d += elm.Ground()
    d += (node1 := elm.Line().left(d.unit*0.5).at(Q1.in1))
    d += elm.Resistor().label('$10k\Omega$', loc='top')
    d += elm.Dot().label('$V_{in}$',loc='left')

    #feedback
    d += elm.Line().up(d.unit).at(node1.end)
    d += elm.Resistor().right(d.unit*2).label('$20k\Omega$')
    d += elm.Line().down(d.unit*1.2)
    
    d += elm.Line().right().at(Q1.out).label('$V_0$',loc='right')

    #biasing
    d += elm.Line().up(d.unit*0.5).at(Q1.vd)
    d += elm.Dot().label('$V_{CC}$')
    d += elm.Line().down(d.unit*0.5).at(Q1.vs)
    d += elm.Dot().label('$V_{EE}$',loc='bottom')
    
    d.save('741opAmp.svg')

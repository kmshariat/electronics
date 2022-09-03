import schemdraw
import schemdraw.elements as elm


with schemdraw.Drawing() as d:
    d.config(inches_per_unit=.5, unit=3)

    d += (Q1 := elm.BjtNpn(circle=True).anchor('collector').color('blue'))
    d += (Lc := elm.Line().up(d.unit/6).at(Q1.collector).dot())
    d += (Rc := elm.Resistor().at(Lc.end).up().label('$R_C$',loc='bot'))
    d += (Lv1 := elm.Line().left(d.unit/2).dot())
    d += (Lv2 := elm.Line().left(d.unit/2))
    d += (R1 := elm.Resistor().down(d.unit/0.715).label('$R_1$',loc='bot').dot())
    d += (Lb := elm.Line().left(d.unit/1.35).at(Q1.base))
    d += (R2 := elm.Resistor().down(d.unit/0.715).at(R1.end).label('$R_2$',loc='bot'))
    d += (Le := elm.Line().down(d.unit/6).at(Q1.emitter).dot())
    d += (Re := elm.Resistor().at(Le.end).down().dot().label('$R_E$',loc='bot'))
    d += (Lbot := elm.Line().left().to(R2.end))
    d += (LnV := elm.Line().up(d.unit/3).at(Lv1.end).dot(open=False).label('$V_{cc}$', loc='right')) 
    d += (LnCs := elm.Line().right(d.unit/2).at(Re.start))

    d += elm.Line().right(d.unit/2).at(Re.end)
    
    d += elm.Capacitor().up().to(LnCs.end).label('$C_E$',loc='bot').color('red')
    d += elm.Capacitor().left().at(Lb.end).label('$C_s$', loc='bot').dot(open=True).label('$V_{in}$',loc='left').color('red')
    d += elm.Capacitor().right().at(Lc.end).label('$C_C$', loc='bot').dot(open=True).label('$V_{out}$',loc='right').color('red')
    d += elm.Ground(lead=True).at(Re.end)

    d.save('VoltageDividerConfig.svg')

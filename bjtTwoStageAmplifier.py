#importing schemdraw module for circuit designing purposes

import schemdraw
import schemdraw.elements as elm


with schemdraw.Drawing() as d:
    d.config(inches_per_unit=.5, unit=3)
    d += (Q1 := elm.BjtNpn(circle=True).anchor('collector').label('$Q_1$')) # drawing the BJT first at setting its collector as one basepoint
    d += (Lc := elm.Line().up(d.unit/6).at(Q1.collector).dot()) #connecting the whole circuit with BJT's collector point
    d += (Rc := elm.Resistor().at(Lc.end).up().label('$R_C$', loc = 'bot'))
    d += (Lv1 := elm.Line().left(d.unit/2))
    d += (Lv2 := elm.Line().left(d.unit/2))
    d += (R1 := elm.Resistor().down(d.unit/0.715).label('$R_1$', loc='bot').dot())
    d += (Lb := elm.Line().left(d.unit/1.35).at(Q1.base))
    d += (R2 := elm.Resistor().down(d.unit/0.715).at(R1.end).label('$R_2$', loc='bot'))
    d += (Le := elm.Line().down(d.unit/6).at(Q1.emitter).dot()) #connecting the whole circuit with BJT's emitter point
    d += (Re := elm.Resistor().at(Le.end).down().dot().label('$R_E$',loc='bot'))
    d += (Lbot := elm.Line().left().to(R2.end)) 
    
    # adding Vcc to the design 
    d += elm.Line().at(Rc.end).right(d.unit/2).dot()
    d += elm.Line().up(d.unit/3).dot().label('$+V_{cc}$',loc='right')
    
    d += (LnCs := elm.Line().right(d.unit/2).at(Re.start))
    d += elm.Line().right(d.unit/2).at(Re.end)
    d += elm.Capacitor2().up().to(LnCs.end)
    
    # adding ac voltage source to the circuit
    d += elm.Capacitor2().left().at(Lb.end)
    d += elm.Resistor().left(d.unit/2).label('$R_G$',loc='bot')
    d += elm.Line().down(d.unit/3.51)
    d += elm.SourceSin().down().label('V$_g$', loc='top')
    d += elm.Line().down(d.unit/8.7)
    d += elm.Line().right(d.unit*1.5)
    
    d += (TSc := elm.Capacitor2().right().at(Lc.end).dot())
    d += elm.Ground(lead=True).at(Re.end)

    d += (TSr := elm.Resistor().at(TSc.end).up().label('$R_1$', loc='bot').dot())
    d += elm.Line().left().dot()
    d += (TSl := elm.Line().at(TSr.start).down(d.unit/2.5))
    d += elm.Line().right(d.unit/1.5)
    d += (TSB := elm.BjtNpn(circle=True).anchor('base').label('$Q_2$'))
    d += (TSC := elm.Line().up(d.unit/6).at(TSB.collector).dot()) # drawing the BJT first at setting its collector as one basepoint
    d += (TSR := elm.Resistor().at(TSC.end).up().label('$R_C$', loc = 'bot'))
    d += (TSL := elm.Line().left())
    d += (TSE := elm.Line().down(d.unit/6).at(TSB.emitter).dot()) # drawing the BJT first at setting its emitter as one basepoint
    d += (TSR := elm.Resistor().at(TSE.end).down().label('$R_E$', loc = 'bot'))
    d += elm.Line().left(d.unit*2)
    d += (TSL := elm.Line().at(TSr.start).down(d.unit*0.79))
    d += elm.Resistor().down().label('$R_2$',loc='bot')
    
    d += elm.Line().at(TSC.end).right(d.unit*0.2)
    d += (TLC := elm.Capacitor2())
    d += elm.Resistor().at(TLC.end).down().label('$R_l$',loc='bot')
    d += elm.Line().down(d.unit/1.255)
    d += elm.Line().left(d.unit*1.5)
    
    #adding the bypass capacitor 
    d += elm.Line().at(TSE.start).down(d.unit/6)
    d += elm.Line().right(d.unit/2)
    d += elm.Capacitor2().down()
    
    #save
    d.save('TwoStageVoltageDividerBias.svg')


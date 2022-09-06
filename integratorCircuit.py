import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config(inches_per_unit=.5, unit=3)
    d += (amp := elm.Opamp()) #starting with the op-amp
    d += (node1 := elm.Line().left(d.unit/2).at(amp.in1).dot())
    d += elm.Resistor().left().label('$R_{in}$') #drawing the input resistor to control the current flow
    d += elm.Dot().label('$V_{in}$') #input signal

    d += elm.Line().left(d.unit/2).at(amp.in2) #inverting the op-amp
    d += elm.Line().down(d.unit/2)
    d += elm.Ground()

    d += elm.Line().right(d.unit).at(amp.out) #output signal
    d += elm.Dot().label('$V_{out}$')

    d += elm.Line().up(d.unit/2).at(node1.end)
    d += elm.Capacitor().right(d.unit*1.5).label('$V_c$') #feedback capacitor
    d += elm.Line().down(d.unit*0.7).dot()
    
    #saving the circuit figure
    d.save('integratorCircuit.svg')

print('a.x²=b.x+c')
a=int(input('Escolha o valor para a: '))
b=int(input('Escolha o valor para b: '))
c=int(input('Escolha o valor para c: '))
print('{}.x²+({}).x+({})'.format(a,b,c))
delta=b**2-4*a*c
print('delta = b²-4*a*c')
print('delta = ({})²-4*({})*({})'.format(b,a,c))
print('delta=', delta)
print('x1=(-b+delta**(1/2)/(2*a)')
print('x1=(-({})+{}**(1/2)/(2*{})'.format(b,delta,a))
x1=(-b+delta**(1/2))/(2*a)
print('x1=',x1)
print('x2=(-b-delta**(1/2))/(2*a)')
print('x2=(-({})-{}**(1/2)/(2*{})'.format(b,delta,a))
x2=(-b-delta**(1/2))/(2*a)
print('x2=',x2)



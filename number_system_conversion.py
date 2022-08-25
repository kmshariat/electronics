#decimal to binary number conversion using recursion
def d2b(number):
    if(number > 1):
        d2b(number//2)
    print(number%2, end=' ')

#binary to decimal number conversion using while loop
def b2d(number):
  decimal, i = 0, 0
  while(number != 0):
    dec = number % 10
    decimal = decimal + dec * pow(2, i)
    number = number//10
    i += 1
  print(decimal)

#binary to decimal number conversion using format specifier 
def b2d2(number):
  print('{0:b}'.format(number))

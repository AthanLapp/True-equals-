mport cmath
import math

io = 1j
xo = (((2**0.5)/(2**0.5))**0.5*io)

print('1i == (((2**0.5)/(2**0.5))**0.5*i)', io==xo)

ix = io**2
xx = xo**2
print('prevprev^2 ==prev^2', ix==io)

print('so... True = False... '
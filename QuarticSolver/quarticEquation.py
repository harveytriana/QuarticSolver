#===================================
# VISIONARY S.A.S.
# harvey.triana@visionary-saas.com 
#===================================
from math import sqrt
from cubicEquation import CubicEquation

class QuarticEquation():
    """
    Quartic Equations Solver
    References:
    Paper: A Note on the Solution of Quartic Equations
    By Herbert E. Salzer Quartic Equations
    Am. Math Society Proceedings, 1959.
    Modified here for support all cases.
    Others
    https:#en.wikipedia.org/wiki/Quadratic_equation
    """
    def Solve(a, b, c, d, e, display = False):
        # validate if is quartic equation
        if a == 0: return None

        # validate zero in float world
        is_zero = lambda x: abs(x) < 1.0E-8

        A = b / a     
        B = c / a     
        C = d / a     
        D = e / a     
        # First, get the resolvent cubic equation, x^3 + C2x^2 + C1x + C0 = 0
        # (C sufix)
        C3 = 1     
        C2 = -B     
        C1 = A * C - 4 * D     
        C0 = D * (4 * B - A * A) - C * C     

        cr = CubicEquation.Solve(C3, C2, C1, C0)

        if cr == None:
            return None
        if is_zero(cr[0].imag):
           x1 = cr[0].real
        elif is_zero(cr[1].imag):
           x1 = cr[1].real
        elif is_zero(ce[2].imag):
           x1 = cr[2].real
        else:
            return None

        m = sqrt(abs(A * A / 4 - B + x1))
        if is_zero(m): 
           m = 0
           n = sqrt(x1 * x1 / 4 - D)
        else:
           n = (A * x1 - 2 * C) / (4 * m)

        alpha = A * A / 2 - x1 - B
        beta = 4 * n - A * m
        t1 = alpha + beta
        t2 = alpha - beta
        gamma = sqrt(abs(t1))
        delta = sqrt(abs(t2))

        if t1 < 0 and t2 >= 0: # gamma is imag and delta is real
            r1 = (-A / 2 + m) / 2 # imag and r2=Conjugate(r1)
            i1 = gamma / 2
            r2 = r1
            i2 = -i1
            r3 = (-A / 2 - m + delta) / 2 # real
            i3 = 0
            r4 = (-A / 2 - m - delta) / 2 # real
            i4 = 0
        elif t1 < 0 and t2 < 0:  # gamma and delta are imag
            r1 = (-A / 2 + m) / 2
            i1 = gamma / 2
            r2 = r1
            i2 = -i1
            r3 = (-A / 2 - m) / 2
            i3 = delta / 2
            r4 = r3
            i4 = -i3
        elif t1 >= 0 and t2 < 0: # gamma is real and delta is imag
            r1 = (-A / 2 + m + gamma) / 2
            i1 = 0
            r2 = (-A / 2 + m - gamma) / 2
            i2 = 0
            r3 = (-A / 2 + m) / 2
            i3 = delta / 2
            r4 = r3
            i4 = -i3
        else: # gamma and delta are reals, then all roots are reals
            r1 = (-A / 2 + m + gamma) / 2
            i1 = 0
            r2 = (-A / 2 - m + delta) / 2
            i2 = 0
            r3 = (-A / 2 + m - gamma) / 2
            i3 = 0
            r4 = (-A / 2 - m - delta) / 2
            i4 = 0

         # built complex roots
        result = [
            complex(r1, i1),
            complex(r2, i2),
            complex(r3, i3),
            complex(r4, i4)
            ]

        if display:
            print('\nQuartic Coefficients')
            print('a : ', a)
            print('b : ', b)
            print('c : ', c)
            print('d : ', d)
            print('e : ', e)
            print('Roots')
            print('z1: ', result[0])
            print('z2: ', result[1])
            print('z3: ', result[2])
            print('z4: ', result[3])

        # output
        return result


         
#===================================
# © Copyright.  VISIONARY S.A.S.
#===================================
from math import atan, cos, sqrt, pi

class CubicEquation():
    """
    Cubic Equation Solver
    """
    def Solve(a, b, c, d, display=False):
        # validate if is cubic equation
        if a == 0: return None
        
        # cube root
        T = 1.0 / 3.0
        crt = lambda x: x ** T if x >= 0 else -(-x) ** T
        # validate zero in float world
        is_zero = lambda x: abs(x) < 1.0E-8

        # constants
        j = b / a
        k = c / a
        l = d / a
        p = -(j * j / 3) + k
        q = (2 / 27 * j ** 3) - (j * k / 3) + l
        t = q ** 2 / 4 + p ** 3 / 27

        if is_zero(t): t = 0

        # There are three cases according to the value of t
        if t > 0: # one real, two complexs
            # real root
            r1 = crt(-q / 2 + sqrt(t)) + crt(-q / 2 - sqrt(t))
            # two complex roots
            r2 = -r1 / 2
            r3 = r2 # conjugated
            # imaginary
            i = sqrt(abs(r1 ** 2 / 4 + q / r1))
            i1 = 0
            i2 = i
            i3 = -i
        elif t == 0: # three real roots, at least two equal
            r1 = 2 * crt(-q / 2)
            r2 = -r1 / 2 + sqrt(r1 ** 2 / 4 + q / r1)
            r3 = -r1 / 2 - sqrt(r1 ** 2 / 4 + q / r1)
            i1 = 0
            i2 = 0
            i3 = 0
        elif t < 0: # three real roots
            x = -q / 2
            y = sqrt(-t)
            angle = atan(y / x)
            if q > 0: angle = pi - angle
            r1 = 2 * sqrt(-p / 3) * cos(angle / 3)
            r2 = 2 * sqrt(-p / 3) * cos((angle + 2 * pi) / 3)
            r3 = 2 * sqrt(-p / 3) * cos((angle + 4 * pi) / 3)
            i1 = 0
            i2 = 0
            i3 = 0
        # built complex roots
        result = [complex(r1 - j / 3, i1),
            complex(r2 - j / 3, i2),
            complex(r3 - j / 3, i3)]

        if display:
            print('\nCubic Coefficients')
            print('a : ', a)
            print('b : ', b)
            print('c : ', c)
            print('d : ', d)
            print('Roots')
            print('z1: ', result[0])
            print('z2: ', result[1])
            print('z3: ', result[2])

        # output
        return result
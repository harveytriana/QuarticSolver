#===================================
# © Copyright.  VISIONARY S.A.S.
# SAMPLES MODULE
#===================================
import quarticEquation as qe
import cubicEquation as ce

print('DEMO')
print('Python Sample')

# CUBIC
# wait: 3+2i, 3-2i, 3, -2
qe.QuarticEquation.Solve(1.0,-7.0, 13.0, 23.0,-78.0, True)

# CUBIC
# wait: -2, i, -i
ce.CubicEquation.Solve(1.0, 2.0, 1.0, 2.0, True)

print('')

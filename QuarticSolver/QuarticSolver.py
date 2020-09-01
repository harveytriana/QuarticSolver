#===================================
# © Copyright.  VISIONARY S.A.S.
# DEBUG MODULE
#===================================
import consoleStyle as echo
import quarticEquation as qe

echo.Green('QUARTIC EQUATION\n')

echo.Yellow('Data input:')

echo.Gray('f(x) = ax**4 + bx**3 + cx**2 + dx + e\n')

coe = []

# USER INPUT
while True:
    input_string = input("Enter list [a, b, c, d, e] separated by space: ")

    user_list = input_string.split()

    # input validation
    e = ''

    if user_list == []:
        break

    n = len(user_list)
    if n < 5 or n > 5:
        e = 'Bad coe number (' + str(n) + ')... Use 5'

    for x in user_list:
        if  x.isalpha(): 
            error = 'Bad coeficient: ' + x
    
    if e == '':
        for x in user_list:
            coe.append(float(x))
        # or use list comprehension...
        # coe = [float(x) for x in user_list]

        if coe[0] == 0.0:
            e = 'Coefficient a can not be 0'
            
    if e == '':
        break
    else:
        echo.Red('Invalid data: ' + e)

# OUTOUT
if not coe == []:
    qe.CubicEquation.Solve(coe[0], coe[1], coe[2], coe[3], True)
else:
    print('Nothing to do.')



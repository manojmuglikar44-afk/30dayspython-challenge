def Add_num(a,b):
    sum = a+b
    print(sum)
Add_num(5,6)
---> 11

def area_of_circle(r):
    pi = 3.14159265
    area = pi*r*r
    return(area)
print(area_of_circle(5))
---> 78.53981625

def Add_all_nums(*num):
    sum = 0
    for value in num:
        if type(value) == int:
            sum = sum + value
        else:
            print('BSDK kuch bhi mat daal!!!... ')
    return sum
print(Add_all_nums(1, 6, 5))
print(Add_all_nums(1,'m',3))
---> BSDK kuch bhi mat daal!!!... 
12

def temp(c):
    fehrn = (c*(9/5))+32
    print(fehrn)
temp(25)
---> 77

def check_season(month):
    month = str(month).strip().lower()
    if month in ['december', 'january', 'february', '12', '1', '2']:
        return 'Winter'
    elif month in ['march', 'april', 'may', '3', '4', '5']:
        return 'Spring'
    elif month in ['june', 'july', 'august', '6', '7', '8']:
        return 'Summer'
    elif month in ['september', 'october', 'november', '9', '10', '11']:
        return 'Autumn'
    else:
        return 'Invalid month'
print(check_season('may'))
print(f'Entered month is in {check_season('may')}')
---> Spring
Entered month is in Spring

def calculate_slope(a,m,c):  # with comparing ay=mx+c
    if m == 0:
        print('Your Equation is not a Straight line')
    elif a == 0:
        print(f'The slope of line is {m}')
    else :
        slope = m/a
        print(f'The slope of line is {slope}')
print(calculate_slope(1,2,3))
print(calculate_slope(0,2,3))
print(calculate_slope(1,0,3))
---> The slope of line is 2.0
None
The slope of line is 2
None
Your Equation is not a Straight line
None

def calculate_slope(a,b,c):  # with comparing ax² + bx + c = 0
    d = ((b*b) - 4*a*c)
    root_1 = (-b + d)/2*a
    root_2 = (-b - d)/2*a
    if d >= 0:
        if a == 0:
            print('Your Equation is not quaadratic')
            x = -c/b
            print(f'Solution of given Equation is {x}')
        elif b == 0:
            i = (-c)**0.5
            print(f'Solution of given Equation is {i}')
        else :
            print(f'Solution of given Quadratic Equation is {root_1} and {root_2}')
    else :
        print('Your solutions are Imaginary')
print(calculate_slope(1,2,5)) # Imaginary
print(calculate_slope(1,5,6)) # -2 , -3
print(calculate_slope(0,2,3)) # -1.5
print(calculate_slope(1,0,-4)) # 2
---> Your solutions are Imaginary
None
Solution of given Quadratic Equation is -2.0 and -3.0
None
Your Equation is not quaadratic
Solution of given Equation is -1.5
None
Solution of given Equation is 2.0
None

def print_list(*list):                       def print_list(*n):
    for n in list:             or                return list(n)
        print(n)                           print(print_list(1,2,3,4))
print(print_list(1,2,3,4))
---> 1                                     -->  [1, 2, 3, 4]
2
3
4



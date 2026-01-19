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


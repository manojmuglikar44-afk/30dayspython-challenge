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

def reverse_list(arr):
    rev_arr = []
    for i in range(len(arr) - 1, -1, -1):
        rev_arr.append(arr[i])
    return rev_arr
print(reverse_list([1, 2, 3, 4, 5]))  
print(reverse_list(["A", "B", "C"]))  
--->[5, 4, 3, 2, 1]
['C', 'B', 'A']

def capitalize_list_item(list):
    or_list = input("Enter elements separated by space: ").split()
    capitalize_list = []
    for word in or_list:
        capitalize_list.append(word.capitalize())
    print(capitalize_list)
capitalize_list_item(list)
---> Enter elements separated by space: a b c d e f
['A', 'B', 'C', 'D', 'E', 'F']

def add_item(list,item):
    list.append(item)
    return list
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff,'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))
---> ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']
[2, 3, 7, 9, 5]

def remove_item(list,item):
    list.remove(item)
    return list
food_stuff = ['Potato','Tomato','Mango','Milk']
print(remove_item(food_stuff,'Mango'))
numbers = [2,3,7,9]
print(remove_item(numbers, 3))
---> ['Potato', 'Tomato', 'Milk']
[2, 7, 9]

def sum_of_numbers():
    num = int(input('Enter the number to add up to :'))
    sum = 0
    for i in range(num + 1):
        sum = sum + i
    print(sum)
sum_of_numbers()
---> Enter the number to add up to :5
15
Enter the number to add up to :10
55
Enter the number to add up to :100
5050

def sum_of_odds():
    num = int(input('Enter a number : '))
    sum = 0
    for i in range(1, num + 1):
        if i % 2 != 0:   
            sum += i
    return sum
print(sum_of_odds())  
---> Enter a number : 8
16
Enter a number : 9
25

def sum_of_even():
    num = int(input('Enter a number : '))
    sum = 0
    for i in range(1, num + 1):
        if i % 2 == 0:   
            sum += i
    return sum
print(sum_of_even())
---> Enter a number : 5
6
Enter a number : 6
12

def evens_and_odds(n):
    evens = []
    odds = []
    for i in range(n+1):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    print("Total evens:", len(evens))
    print("Total odds:", len(odds))
    return evens, odds
all_evens, all_odds = evens_and_odds(100)
---> Total evens: 51
Total odds: 50

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(f'Factorial of {n} is {fact}')
    return fact
factorial(5)
---> Factorial of 5 is 120

def is_empty(value):
    return not bool(value)
print(is_empty(""))
print(is_empty([]))        
print(is_empty({}))        
print(is_empty("Hello"))   
print(is_empty([1, 2, 3])) 
---> True
True
True
False
False

def calculate_mean(data):
    return sum(data)/len(data)




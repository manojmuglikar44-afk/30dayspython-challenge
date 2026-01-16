>>> age=int(19)
>>> print(age)
19

>>> height=float(3.14)
>>> print(height)
3.14

>>> x=1+7j
>>> print(x)
(1+7j)

>>> base=int(input("Enter Base : "))
Enter Base : 20
>>> height=int(input("Enter Height : "))
Enter Height : 10
>>> print(f"The area of the triangle is {0.5*base*height}" )
The area of the triangle is 100

>>> a = int(input("Enter side a : "))
Enter side a : 5
>>> b = int(input("Enter side b : "))
Enter side b : 4
>>> c = int(input("Enter side c : "))
Enter side c : 3
>>> print(f"The perimeter of the triangle is {a+b+c}")
The perimeter of the triangle is 12

>>> length = int(input("Enter Length : "))
Enter Length : 54
>>> width = int(input("Enter Width : "))
Enter Width : 46
>>> print(f"The perimeter of Rectangle is {lenghth*width}")
The perimeter of Rectangle is 2484
>>> print(f"The perimeter of Rectangle is {2*(length+width)}")
The perimeter of Rectangle is 200

>>> r = int(input("Enter the Radius of circle : "))
Enter the Radius of circle : 6
>>> print(f"The Area of Circle is {3.14*(r**2)}")
The Area of Circle is 113.04
>>> print(f"The Circumference of Circle is {2*3.14*r}")
The Circumference of Circle is 37.68

>>> #in y = mx + c , m is slope
>>> m = 2
>>> y = -2
>>> x = -y/m
>>> print("Slope is ",m)
Slope is  2
>>> print("x intercept is",x)
x intercept is 1.0
>>> print("y intercept is",y)
y intercept is -2

>>> x1,y1=2,2
>>> x2,y2=6,10
>>> print("The Slope of the line is",(y2-y1)/(x2-x1))
The Slope of the line is 2.0
>>> print("The Euclidean Distance is",(((x2-x1)**2)+((y2-y1)**2))**0.5)
The Euclidean Distance is 8.94427190999916

>>> if m>(y2-y1)/(x2-x1):
...     print("task 1 slope is greater than task 2 slope")
... else:
...     print("task 2 slope is greater than task 1 slope")
...
task 2 slope is greater than task 1 slope

>>> for x in range(-10,10):
...     y = x**2 + 6*x + 9
...     if y==0:
...         print("x =",x)
...         print("y =",y)
...
x = -3
y = 0

>>> len_python=len("python")
>>> len_dragon=len("dragon")
>>> print("len_python",len_python)
len_python 6
>>> print("len_python =",len_python)
len_python = 6
>>> print("len_dragon =",len_dragon)
len_dragon = 6 

>>> print('on' in 'dragon' and 'on' in 'python')
True

>>> print('jargon' in 'I hope this course is not full of jargon')
True

>>> print('on'not in 'dragon' and 'on' not in 'python')
False

>>> len_python = len('python')
>>> print(len_python)
6
>>> float_length = float(len_python)
>>> print(float_length)
6.0
>>> string_length = str(len_python)
>>> print(string_length)
6

>>> num = int(input("Enter the Number = "))
Enter the Number = 5
>>> if num % 2 == 0:
...     print(f'{num} is even')
... else:
...     print(f'{num} is odd')
...
5 is odd 

>>> floor_div = 7 // 3
>>> print(floor_div)
2
>>> converted_value = int(2.7)
>>> print(converted_value)
2
>>> print('floor_div' == 'converted_value')
False

>>> type(10)
<class 'int'>
>>> type('10')
<class 'str'>
>>> print(type(10)==type('10'))
False

>>> num1 = int(9.8)
>>> num2 = 10
>>> print(num1==num2)
False

>>> hours = int(input("Enter hours: "))
Enter hours: 40
>>> rph = int(input("Enter rate per hour: "))
Enter rate per hour: 28
>>> print('Your weekly earning is',hours*rph)
Your weekly earning is 1120

>>> print('Your weekly earning is',hours*rph)
Your weekly earning is 1120
>>> years = int(input('Enter number of years you have lived:'))
Enter number of years you have lived:100
>>> seconds_lived = years*365*24*60*60
>>> print(f'You have lived for {seconds_lived} seconds.')
You have lived for 3153600000 seconds.

>>> for i in range(1,6):
...      print(1,i**0,i**1,i**2,i**3)
...
1 1 1 1 1
1 1 2 4 8
1 1 3 9 27
1 1 4 16 64
1 1 5 25 125







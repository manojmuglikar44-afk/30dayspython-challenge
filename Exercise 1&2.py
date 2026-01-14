#Day 2: 30 Days of python programming
First_name="Manoj"
Last_name="Muglikar" 
Full_name="Manoj Muglikar"
Country="India"
City="Pune"
Age=19
Year=2026
is_married="no"
is_true=(True)
is_light_on=""
a,b,c,d=1,2,3,4

#Level 2

print(type(First_name))
print(type(Last_name),type(Full_name),type(is_true))
print(len(First_name))
First_name="Manoj"
Last_name="Muglikar" 
len1=len(First_name)
len2=len(Last_name)
print(len1,len2)
if len1 > len2:
    print(f"{first_name} is longer")
else:
    print(f"{Last_name} is longer")

num_one=5
num_two=4
total =num_one+num_two
diff = num_two - num_one 
multiply = num_one * num_two
division = num_one / num_two 
remainder = num_two % num_one
exp = num_one**num_two
floor_division = num_one//num_two
print(f"total={total}\ndiff={diff}\nmultiply={multiply}\ndivision={division}\nremainder={remainder}\nexp={exp}\nfloor_division={floor_division}\n")

r=30
area_of_circle=3.14*(r**2)
print(area_of_circle)

r=30
circumference_of_circle=2*3.14*r
print(circumference_of_circle)

r=int(input("Enter any value for radius = "))
print(r)
area_of_circle=3.14*(r**2)
print(area_of_circle)

First_name=input("Enter your First Name :")
Last_name=input("Enter your Last Name :")
Country=input("Enter your Country :")
Age=int(input("Enter your Age :"))
print(f"First_name = {First_name}\nLast_name = {Last_name}\nCountry={Country}\nAge={Age}")

help('keywords')

OUTPUTS:
<class 'str'>
<class 'str'> <class 'str'> <class 'bool'>
5
5 8
Muglikar is longer
total=9
diff=-1
multiply=20
division=1.25
remainder=4
exp=625
floor_division=1

2826.0
188.4
Enter any value for radius = 5
5
78.5
Enter your First Name :manoj
Enter your Last Name :muglikar
Enter your Country :india
Enter your Age :19
First_name = manoj
Last_name = muglikar
Country=india
Age=19

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return        
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not

#💻 Exercises: Day 9
#Level 1

age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to learn to drive.')
else :
    print(f'You need {18-age} more years to learn to drive')
--->Enter your age: 20
You are old enough to learn to drive.
Enter your age: 10
You need 8 more years to learn to drive

my_age = 19 
your_age = int(input("Enter your age: "))
if your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print(f"You are {diff} year older than me.")
    else:
        print(f"You are {diff} year older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    if diff == 1:
        print(f"I am {diff} year older than you")
    else:
        print(f"I am {diff} year older than you")
else:
    print("We are the same age")
----> 
Enter your age: 5
I am 14 year older than you

a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b :
    print(f'{a} is greater than {b}')
elif a==b :
    print(f'{a} is equal to {b}')
else :
    print(f'{a} is smaller than {b}')
---> Enter number one: 5
Enter number two: 4
5 is greater than 4

# Exercises: Level 2

score = int(input('Enter your score: '))
if score >= 90 and score < 100:
    print('You have Scored A grade')
elif score >= 80 and score < 90:
    print('You have Scored B grade')
elif score >= 70 and score < 80:
    print('You have Scored C grade')
elif score >= 60 and score < 70:
    print('You have Scored D grade')
else : 
    print('You have Scored F grade')
---> Enter your score: 60
You have Scored D grade
Enter your score: 50
You have Scored F grade

month = input('Enter Month: ')
Autumn = ('September','October','November')
Winter = ['December','January','February']
Spring = ['March','April','May']
Summer = ['June','July','August']
if month in Autumn:
    print('season is Autumn')
elif month in Winter:
    print('season is Winter')
elif month in Spring:
    print('season is Spring')
else:
    print('Entered month is wrong')
---> Enter Month: May
Enter Month: August
Season is Summer
season is Spring

fruits = ['banana', 'orange', 'mango', 'lemon']
i = input('Enter Fruit name: ')
if i in fruits: 
    print('That fruit already exist in the list')
else:
    fruits.append(i)
    print(fruits)
---> Enter Fruit name: Apple
['banana', 'orange', 'mango', 'lemon', 'Apple']
Enter Fruit name: orange
That fruit already exist in the list

# Exercises: Level 3





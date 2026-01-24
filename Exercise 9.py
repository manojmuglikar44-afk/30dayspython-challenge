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
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    mid_skill = len(skills) // 2
    print("Middle skill:", skills[mid_skill])

if 'skills' in person:
    if 'Python' in person['skills']:
        print("Python skill found")
    else:
        print("Python skill not found")

if 'skills' in person:
    skills = person['skills']
    if set(skills) == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif set(skills) >= {'Node', 'Python', 'MongoDB'}:
        print("He is a backend developer")
    elif set(skills) >= {'React', 'Node', 'MongoDB'}:
        print("He is a fullstack developer")
    else:
        print("Unknown title")

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. "
          f"He is married.")
---> Middle skill: Node
Python skill found!
He is a backend developer
Asabeneh Yetayeh lives in Finland. He is married.

Questions :

#Exercises: Level 1

1.Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough 
to drive. If below 18 give feedback to wait for the missing amount of years. Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.

    
2.Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use 
input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 
year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
Output:
Enter your age: 30
You are 5 years older than me.
3.Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
Enter number one: 4
Enter number two: 3
4 is greater than 3

#Exercises: Level 2

1.Write a code which gives grade to students according to theirs scores:
```sh
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
```
2.Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If 
the user input is: September, October or November, the season is Autumn. December, January or 
February, the season is Winter. March, April or May, the season is Spring June, July or August, the 
season is Summer
3.The following list contains some fruits:
```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')

#Exercises: Level 3

1.Here we have a person dictionary. Feel free to modify it!
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:







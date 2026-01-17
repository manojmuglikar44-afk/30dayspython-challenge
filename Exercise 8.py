dog = {}
print(dog)
---> {}

dog['name'] = 'Bob'
dog['color'] = 'Brown'
dog['breed'] = 'Bull Dog'
dog['legs'] = 2
dog['Age'] = 100 
print(dog)
---> {'name': 'Bob', 'color': 'Brown', 'breed': 'Bull Dog', 'legs': 2, 'Age': 100}

student = {}
student['first_name'] = 'Person'
student['last_name'] = 'Unknown'
student['gender'] = 'Pata nahi'
student['age'] = 'nahi bataunga'
student['marital status'] = 'nahi hui'
student['skills'] = 'Timepass'
student['country'] = 'yahi'
student['city'] = 'wohi'
student['address'] = 'kahi bhi'
print(student)
---> {'first_name': 'Person', 'last_name': 'Unknown', 'gender': 'Pata nahi', 'age': 'nahi bataunga', 'marital status': 'nahi hui', 'skills': 'Timepass', 'country': 'yahi', 'city': 'wohi', 'address': 'kahi bhi'}

print(len(student))
---> 9

skills = student['skills']
print(skills)
print(type(skills))
--->['Timepass', 'Avarapanti', 'Overthinking']
<class 'list'>

student['skills'].append('Avarapanti')
student['skills'].append('Overthinking')
print(student)
---> {'first_name': 'Person', 'last_name': 'Unknown', 'gender': 'Pata nahi', 'age': 'nahi bataunga', 'marital status': 'nahi hui', 'skills': ['Timepass', 'Avarapanti', 'Overthinking'], 'country': 'yahi', 'city': 'wohi', 'address': 'kahi bhi'}

data = student.keys()
print(data)
---> dict_keys(['first_name', 'last_name', 'gender', 'age', 'marital status', 'skills', 'country', 'city', 'address'])

value = student.values()
print(value)
---> dict_values(['Person', 'Unknown', 'Pata nahi', 'nahi bataunga', 'nahi hui', ['Timepass'], 'yahi', 'wohi', 'kahi bhi'])

print(student.items())
---> dict_items([('first_name', 'Person'), ('last_name', 'Unknown'), ('gender', 'Pata nahi'), ('age', 'nahi bataunga'), ('marital status', 'nahi hui'), ('skills', ['Timepass']), ('country', 'yahi'), ('city', 'wohi'), ('address', 'kahi bhi')])

del student['skills']
print(student)
---> {'first_name': 'Person', 'last_name': 'Unknown', 'gender': 'Pata nahi', 'age': 'nahi bataunga', 'marital status': 'nahi hui', 'country': 'yahi', 'city': 'wohi', 'address': 'kahi bhi'}

del student
print(student)
--->  print(student)
          ^^^^^^^
NameError: name 'student' is not defined


Questions : 

# 💻 Exercises: Day 8
1.Create an empty dictionary called dog
2.Add name, color, breed, legs, age to the dog dictionary
3.Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
4.Get the length of the student dictionary
5.Get the value of skills and check the data type, it should be a list
6.Modify the skills values by adding one or two skills
7.Get the dictionary keys as a list
8.Get the dictionary values as a list
9.Change the dictionary to a list of tuples using items() method
10.Delete one of the items in the dictionary
11.Delete one of the dictionaries

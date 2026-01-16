Empty_list = list()
print(Empty_list)
--->[]

list = ['A','B','C','D','E','F','G'] 

list = ['A','B','C','D','E','F','G']
print(len(list))
---> 7

list = ['A','B','C','D','E','F','G']
first_item = list[0]
print(first_item)
second_item = list[3] 
print(second_item)
third_item = list[-1]
print(third_item)

mixed_data_types = ['Manoj','19','168cm','not married','Pune']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
print(it_companies)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
new = '#; '.join(it_companies)
print(new)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(len(it_companies))
---> 7

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
first_item = it_companies[0]
second_item = it_companies[3]
third_item = it_companies[-1]
print(first_item, second_item, third_item)
---> Facebook Apple Amazon

 it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.append('IT company')
print(it_companies)
---> ['Facebook', 'Google','Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'IT company']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.insert(3,'IT company')
print(it_companies)
---> ['Facebook', 'Google', 'Microsoft', 'IT company', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies[1] = it_companies[1].upper()
print(it_companies)
--->   print(it_companies)
          ^^^^^^^^^^^^
NameError: name 'it_companies' is not defined

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
--->['Facebook', 'GOOGLE', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del(it_companies)
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
new_list = front_end + back_end
print(new_list)
---> ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

old_list = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
new_list = old_list.copy()
redux_index = new_list.index('Redux')
new_list.insert(redux_index + 1, 'Python')
new_list.insert(redux_index + 2, 'SQL')
print(new_list)
---> ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'SQL', 'Node', 'Express', 'MongoDB']

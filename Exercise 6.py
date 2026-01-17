empty_tuple = ()

brothers = ('abc','aasd','qwer','sfgb')
sisters = ('dvs','geds','setgb','ergf')

sibling = brothers 

brothers = ('abc','aasd','qwer','sfgb')
sisters = ('dvs','geds','setgb','ergf')
siblings = brothers + sisters
print(siblings)
---> ('abc', 'aasd', 'qwer', 'sfgb', 'dvs', 'geds', 'setgb', 'ergf')

siblings = brothers + sisters
print(siblings)
print('number of siblings =',len(siblings))
---> number of siblings = 8

parents = ('jvhs','jvcvs')
family_members = siblings + parents
print(family_members)
---> ('abc', 'aasd', 'qwer', 'sfgb', 'dvs', 'geds', 'setgb', 'ergf', 'jvhs', 'jvcvs')

family_members = ('abc', 'aasd', 'qwer', 'sfgb', 'dvs', 'geds', 'setgb', 'ergf', 'jvhs', 'jvcvs')
parents = family_members[-2:]   
siblings = family_members[:8]  
print("Siblings:", siblings)
print("Parents:",parents)
---> Siblings: ('abc', 'aasd', 'qwer', 'sfgb', 'dvs', 'geds', 'setgb', 'ergf')
Parents: ('jvhs', 'jvcvs')

fruits = ('mango','banana','apple','grapes')
vegetables = ('potato','tomato','brinjal','onion')
animal_products = ('egg','milk','meat')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
---> ('mango', 'banana', 'apple', 'grapes', 'potato', 'tomato', 'brinjal', 'onion', 'egg', 'milk', 'meat')

food_stuff_tp=('mango', 'banana', 'apple', 'grapes', 'potato', 'tomato', 'brinjal', 'onion', 'egg', 'milk', 'meat')
food_stuff_lt = list(food_stuff_tp)
m_l= len(food_stuff_lt)//2
print(m_l)
print(food_stuff_lt)
print(food_stuff_lt[:m_l] +food_stuff_lt[m_l+1:])
---> 5
['mango', 'banana', 'apple', 'grapes', 'potato', 'tomato', 'brinjal', 'onion', 'egg', 'milk', 'meat']
['mango', 'banana', 'apple', 'grapes', 'potato', 'brinjal', 'onion', 'egg', 'milk', 'meat']

food_stuff_tp=('mango', 'banana', 'apple', 'grapes', 'potato', 'tomato', 'brinjal', 'onion', 'egg', 'milk', 'meat')
food_stuff_lt = list(food_stuff_tp)
print('First 3 items =',food_stuff_lt[:3])
print('Last 3 items =',food_stuff_lt[8:])
---> First 3 items = ['mango', 'banana', 'apple']
Last 3 items = ['egg', 'milk', 'meat']


food_stuff_tp = ('mango', 'banana', 'apple', 'grapes', 'potato', 'tomato', 'brinjal', 'onion', 'egg', 'milk', 'meat')
del(food_stuff_tp)
print(food_stuff_tp)
---> print(food_stuff_tp)
          ^^^^^^^^^^^^^
NameError: name 'food_stuff_tp' is not defined

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
---> False
True



Questions : 

#Exercises: Level 1

1.Create an empty tuple
2.Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
3.Join brothers and sisters tuples and assign it to siblings
4.How many siblings do you have?
5.Modify the siblings tuple and add the name of your father and mother and assign it to family_members

#Exercises: Level 2

1.Unpack siblings and parents from family_members
2.Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
3.Change the about food_stuff_tp tuple to a food_stuff_lt list
4.Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
5.Slice out the first three items and the last three items from food_stuff_lt list
6.Delete the food_stuff_tp tuple completely
7.Check if an item exists in tuple:
  Check if 'Estonia' is a nordic country
  Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

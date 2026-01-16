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

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)                       # incomplete
---> ['mango', 'banana', 'apple', 'grapes', 'potato', 'tomato', 'brinjal', 'onion', 'egg', 'milk', 'meat']

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

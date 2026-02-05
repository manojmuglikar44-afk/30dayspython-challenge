#Exercises: Level 1
import random
import string
def user_id_gen_by_user():
    characters = string.ascii_lowercase + string.digits 
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id
print(user_id_gen_by_user())
---> p8b65n

import random
import string
def random_user_id():
    num_char, num_id = map(int,input("Enter the no. of Characters and no. of Id's to Print: ").split())
    for _ in range(num_id):
        characters = string.ascii_lowercase + string.digits 
        user_id = ''.join(random.choice(characters) for _ in range(num_char))
        print(user_id)
print(random_user_id())
---> Enter the no. of Characters and no. of Id's to Print: 5 5
yyh4f
r1c9k
w6wwc
s2tx1
1ejla
Enter the no. of Characters and no. of Id's to Print: 16 5
uxxf8c45rz7wju4y
171yf8jjwyx1c8ro
fk672sc8pgd3o4xw
1v4glrbgsvyw6rdh
gqgc0dqyc566yvvs

import random
def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return f'rgb({r},{g},{b})'
print(rgb_color_gen())
---> rgb(238,184,230)
rgb(242,19,12)

#Exercises: Level 2

import random
def list_of_hexa_colors(count):
  colors = []
  for _ in range(count):
    hex_digits = [random.choice('0123456789abcdef') for _ in range(6)]
    color = '#' + ''.join(hex_digits)
    colors.append(color)
  return colors
print(list_of_hexa_colors(1))
print(list_of_hexa_colors(3))
print(list_of_hexa_colors(5))
---> ['#d0c82d']
['#deaf64', '#ce3673', '#81711a']
['#989557', '#3c373b', '#9a269c', '#05ef65', '#452df4']

import random
def list_of_rgb_colors(count):
  colors = []
  for _ in range(count):
      r = random.randint(0, 255)
      g = random.randint(0, 255)
      b = random.randint(0, 255)
      colors.append((r, g, b))
  return colors
print(list_of_rgb_colors(3))
---> [(149, 146, 33), (249, 95, 180), (184, 211, 65)]

import random
def generate_colors(num, n):
    colors = []
    if num == 'hexa':
        for _ in range(n):
            hex_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            colors.append(hex_color)
    elif num == 'rgb':
        for _ in range(n):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            rgb_color = f"rgb({r},{g},{b})"
            colors.append(rgb_color)
    else:
        raise ValueError("num must be 'hexa' or 'rgb'")
    return colors
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1)) 
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1)) 
--->
['#5b6424', '#eeaf34', '#597291']
['#222f9b']
['rgb(159,217,132)', 'rgb(229,27,34)', 'rgb(60,125,3)']
['rgb(159,218,242)']

#Exercises: Level 3

import random 
def shuffle_list(list):
    lst = list[:]
    random.shuffle(lst)
    return lst

print(shuffle_list([1,2,3,4,5,6,7,8,9,10]))
--->[5, 4, 1, 2, 8, 6, 9, 7, 10, 3]

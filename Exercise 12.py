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

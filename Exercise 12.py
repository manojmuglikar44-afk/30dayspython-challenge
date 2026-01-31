import random
import string
def random_user_id():
    characters = string.ascii_lowercase + string.digits 
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id
print(random_user_id())
---> p8b65n

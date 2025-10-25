import random
import string

def generated_random_password(length=15):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits

    characters = lower_case + upper_case + digits

    
    password = ''.join(random.choice(characters) for _ in range(length))
    p_list = list(password)
    random.shuffle(p_list)
    final = ''.join(p_list)
    return final
random_password = generated_random_password()
print("The random password is", random_password)
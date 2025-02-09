import random
import string

def generate_password(lenght=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(lenght))

print("Generated Password: ", generate_password())
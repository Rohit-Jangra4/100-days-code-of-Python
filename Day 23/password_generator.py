import random
import string

def password_generator(length):
    character= string.ascii_letters+string.digits+string.punctuation

    password=""

    for _ in range(length):
        password += random.choice(character)

    return password

if __name__=="__main__":
    password=password_generator(20)

print("Password Generated:",password)

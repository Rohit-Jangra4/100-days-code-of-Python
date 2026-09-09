
import random
import string


# Encode
def encode_word(word):

    if len(word) < 3:
        return word[::-1]

    else:
        # First letter ko last mein bhejo
        word = word[1:] + word[0]

        # 3 random characters start aur end mein
        prefix = ''.join(random.choices(string.ascii_letters, k=3))
        suffix = ''.join(random.choices(string.ascii_letters, k=3))

        return prefix + word + suffix


# Decode
def decode_word(word):

    if len(word) < 3:
        return word[::-1]

    else:
        # Start aur end ke 3 random characters remove
        word = word[3:-3]

        # Last character ko front mein lao
        word = word[-1] + word[:-1]

        return word


# Main program
choice = input("Enter E for Encode or D for Decode: ").upper()

message = input("Enter message: ")

if choice == "E":

    secret = " ".join(encode_word(word) for word in message.split())

    print("Secret code:", secret)


elif choice == "D":

    decoded_message = " ".join(
        decode_word(word) for word in message.split()
    )

    print("Decoded message:", decoded_message)


else:
    print("Invalid choice!")
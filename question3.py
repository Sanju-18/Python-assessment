import random
value = input()
n = random.randint(1,26)

new_value = chr(64+n)+value[::-1].lower()
print(new_value)
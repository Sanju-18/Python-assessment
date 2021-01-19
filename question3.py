import random
# getting input
value = input()

#generating random value
n = random.randint(1,26)

#inserting random alphabet and reversing the input string
new_value = chr(64+n)+value[::-1].lower()
print(new_value)

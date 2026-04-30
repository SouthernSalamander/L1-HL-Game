import random

secret_list = []
num_generated = 0

while num_generated < 30:
    secret = random.randint(1, 3)
    secret_list.append(secret)
    num_generated += 1

for item in secret_list:
    print(item)
    
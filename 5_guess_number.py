import random

answer = random.randrange(1,10)
guess = int(input("Enter number between 1-10:"))
while answer != guess:
    if guess < answer:
        print("higher")
    else:
        print("smaller")
    guess = int(input("Enter number between 1-10:"))
print("done")
name = "Jacek"
try:
    print(name)
#except NameError:
#    print("Error occured")

except NameError as e:
    print("Error occured: ", e)

try:
    div = 7/0
    print("This is not printed if error occures")
except ZeroDivisionError as e:
    print("Error occured: ", e)
finally:
    print("This is printed even if error occured")

try:
    num = int(input("Enter number > 25 && < 50: "))
    if num < 25:
        raise ValueError("I said bigger than 25!")
    elif num > 50:
        raise ValueError("Nah, bigger than 50!")
    else:
        print("good, my friend")
except ValueError as e:
    print("Error occured: ", e)
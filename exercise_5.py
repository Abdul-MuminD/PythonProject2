print("Welcome to python pizza Deliveries!")
size = input("what type of pizza are you ordering? S, M or L: ")
peperoni =input("Do you want peperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == 'S':
    bill = 15
    print(f"You chose S which is ${bill}")
    if peperoni == 'Y':
        bill +=2
        print("Peperoni is $2")
elif size == 'M':
    bill = 20
    print(f"You chose M which is ${bill}")
    if peperoni == 'Y':
        bill += 3
        print("Peperoni is $3")
elif size == 'L':
    bill = 25
    print(f"You chose L which is ${bill}")
    if peperoni == 'Y':
        bill += 3
        print("Peperoni is $3")
else:
    print("You typed the wrong inputs.")


if extra_cheese == "Y":
    bill += 1
    print("Extra cheese is $1")

print(f"Your final bill is: ${bill}.")





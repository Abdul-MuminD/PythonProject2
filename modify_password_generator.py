import random


letters = ['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator! ")
ne_letters = int(input("How many letter would you like in your password? \n"))
ne_symbols = int(input("How many symbols would you like? \n"))
ne_numbers = int(input("How many numbers would you like? \n"))

password_list = []

for i in range(0, ne_letters):
    password_list.append(random.choice(letters))

for i in range(0,ne_symbols):
    password_list.append(random.choice(symbols))

for i in range(0, ne_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
print(password_list)

password = ''
for letter in password_list:
    password += letter
print(f"Your password is: {password}")
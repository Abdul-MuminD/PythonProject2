import random

letters = "AaBbCcDdEeFfGgIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789@#$%&*"
password = ""

for i in range(12):
    password += random.choice(letters)

print(password)
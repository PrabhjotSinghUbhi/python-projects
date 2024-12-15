import random
import secrets

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")
symbols = list("!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`")

x = [letters, numbers, symbols]

secret = []

print("Welcome to the PyPassword generator")
inLetter = int(input("how many letter would you like in your password?\n"))
inSymbols = int(input("how many symbols would you like?\n"))
inNums = int(input("how many numbers would you like?\n"))

# running for the length of the password inputted by user
for i in range(0, inLetter):
    ran_L = random.randint(0, len(letters) - 1)
    secret.append(
        letters[ran_L],
    )

for i in range(0, inSymbols):
    ran_S = random.randint(0, len(symbols) - 1)
    secret.append(symbols[ran_S])

for i in range(0, inNums):
    ran_N = random.randint(0, len(numbers) - 1)
    secret.append(numbers[ran_N])

random.shuffle(secret)

password = ""
for i in secret:
    password += i

print(f"Your password is {password}")

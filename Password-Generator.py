import random

chars = "abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXY123456789"

while 1:
    password_len = int(input("Length of password: "))
    password_count = int(input("How many pass do you want to generate: "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here is your password: ", password)

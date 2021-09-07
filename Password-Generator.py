import random

print('''   ______   ______    _______   _______ .___________. _______   ______  __    __  
 /      | /  __  \  |       \ |   ____||           ||   ____| /      ||  |  |  | 
|  ,----'|  |  |  | |  .--.  ||  |__   `---|  |----`|  |__   |  ,----'|  |__|  | 
|  |     |  |  |  | |  |  |  ||   __|      |  |     |   __|  |  |     |   __   | 
|  `----.|  `--'  | |  '--'  ||  |____     |  |     |  |____ |  `----.|  |  |  | 
 \______| \______/  |_______/ |_______|    |__|     |_______| \______||__|  |__| 
                                                                                  ''')

chars = str(input ("Name that you want to Generate: "))

while 1:
    password_len = int(input("Length of password: "))
    password_count = int(input("How many pass do you want to generate: "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here is your password: ", password)
        
        with open("password.txt", "a") as file:
            file.write(password + '\n')

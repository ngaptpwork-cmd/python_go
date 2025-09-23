message = ''
while message != 'quit':
    message = input("Please enter a topping you want to get into your pizza ")
    if message != 'quit':
        print(f"I'll add {message} into your pizza!")

flag = True
while flag == True:
    message = input("Please enter a topping you want to get into your pizza ")
    if message == 'quit':
        flag = False
    else:
        print(f"I'll add {message} into your pizza!")

while True:
    message = input("Please enter a topping you want to get into your pizza ")
    if message == 'quit':
        break
    else:
        print(f"I'll add {message} into your pizza!")
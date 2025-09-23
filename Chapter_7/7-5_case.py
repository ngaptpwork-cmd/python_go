
while True:
    prompt = "Please enter your age!"
    prompt += "\nPlease enter quit if you don't want to buy ticket "
    age = input(prompt)
    if age == 'quit':
        break
    age = int (age)
    if age < 3:
        money = 'free'
    elif age <= 12:
        money = '$10'
    elif age > 12:
        money = '$15'
    print(f"The ticket is {money}")
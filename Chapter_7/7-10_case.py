dream_vacations = {}
while True:
    name = input("Please Enter your name: ")
    place = input ("If you could visit one place in the world, where would you go? ")
    dream_vacations[name] = place
    answer = input ("Do you want to take another response? Yes/No ")
    if answer == 'No':
        break
for name,place in dream_vacations.items():
    print(f"{name.title()} want to go to {place.title()}.")
pizza_list = ['Hawaian', 'Bacon', 'Cheese']
# for pizza in pizza_list:
#     print(f"I ate {pizza} at least twice.")
# print("I really like pizza, I wanna taste all of pizza on the world")

friend_pizzas = pizza_list[:]

pizza_list.append('Takoyaki')
friend_pizzas.append('Ebi')

print("My favorite pizzas are:")
for pizza in pizza_list:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
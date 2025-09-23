sandwich_orders = ['chicken', 'pastrami','beef','pastrami','pastrami', 'fish']
print("The deli has run out of pastrami.")
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    if current_sandwich == 'pastrami':
        continue
    else:
        print(f"I made you {current_sandwich} sandwich.")
        finished_sandwiches.append(current_sandwich)
print("These sandwiched below were made:")
for sandwich in finished_sandwiches:
    print(sandwich)

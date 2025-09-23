sandwich_orders = ['chicken', 'beef', 'fish']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made you {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("These sandwiched below were made:")
for sandwich in finished_sandwiches:
    print(sandwich)

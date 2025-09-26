def order(*sandwiches):
    print("Your order sandwiches are:")
    for sandwich in sandwiches:
        print(f"one {sandwich} sanwich")


order("chicken")
order("pizza", "beef")
order("salmond", "sausage", "pork")

human_age = 23
if human_age < 2:
    role = 'a baby'
elif human_age < 4:
    role = 'a toddler'
elif human_age < 13:
    role = 'a kid'
elif human_age < 20:
    role = 'teenager'
elif human_age < 65:
    role = 'an adult'
elif human_age >= 65:
    role = 'an elder'
print(f"That person is {role}.")
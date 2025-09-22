current_users = ['frog','Panda','wolf','angel','elf']
current_users_lower = [user.lower() for user in current_users]
# for user in current_users_lower:
#     print(f"{user}")
new_users = ['anaconda','penguin','panda','evil','snowwhite']

for user in new_users:
    user = user.lower()
    # print (f"{user}")
    if user in current_users_lower:
        print("You need to enter a new username")
    else:
        print ("The username is available")
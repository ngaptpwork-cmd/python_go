guest_list =['Trang Bui', 'Giang', 'Trang Vi','Huy']
print (guest_list[-1])


guest_list[-1] = 'Trang Pham'

print(f"Dear, Ms.{guest_list[0]}, I just found a bigger table")
print(f"Dear, Ms.{guest_list[1]}, I just found a bigger table")
print(f"Dear, Ms.{guest_list[2]}, I just found a bigger table")
print(f"Dear, Ms.{guest_list[-1]}, I just found a bigger table")

guest_list.insert(0,'Hang')
guest_list.insert(2,'Huong')
guest_list.append('Thang')

print(f"\nDear, Ms.{guest_list[0]}, I hope you'll come and have a comfortable time.")
print(f"Dear, Ms.{guest_list[1]}, I hope you'll come and have a comfortable time.")
print(f"Dear, Ms.{guest_list[2]}, I hope you'll come and have a comfortable time.")
print(f"Dear, Ms.{guest_list[3]}, I hope you'll come and have a comfortable time.")
print(f"Dear, Ms.{guest_list[4]}, I hope you'll come and have a comfortable time.")
print(f"Dear, Ms.{guest_list[5]}, I hope you'll come and have a comfortable time.")
print(f"Dear, Ms.{guest_list[-1]}, I hope you'll come and have a comfortable time.")

print(f"\nDear, Ms.{guest_list[0]}, Sorry, because my new dinner table won't arrive in time for the dinner, so I can invite only two people for dinner")
print(f"Dear, Ms.{guest_list[1]}, Sorry, because my new dinner table won't arrive in time for the dinner, so I can invite only two people for dinner")
print(f"Dear, Ms.{guest_list[2]}, Sorry, because my new dinner table won't arrive in time for the dinner, so I can invite only two people for dinner")
print(f"Dear, Ms.{guest_list[3]}, Sorry, because my new dinner table won't arrive in time for the dinner, so I can invite only two people for dinner")
print(f"Dear, Ms.{guest_list[4]}, Sorry, because my new dinner table won't arrive in time for the dinner, so I can invite only two people for dinner")
print(f"Dear, Ms.{guest_list[5]}, Sorry, because my new dinner table won't arrive in time for the dinner, so I can invite only two people for dinner")
print(f"Dear, Ms.{guest_list[-1]}, Sorry, because my new dinner table won't arrive in time for the dinner, so I can invite only two people for dinner")

remove_guest = guest_list.pop()
print (f"\nUnfortunately {remove_guest}, I can't invite you to dinner")
remove_guest = guest_list.pop()
print (f"Unfortunately {remove_guest}, I can't invite you to dinner")
remove_guest = guest_list.pop()
print (f"Unfortunately {remove_guest}, I can't invite you to dinner")
remove_guest = guest_list.pop()
print (f"Unfortunately {remove_guest}, I can't invite you to dinner")
remove_guest = guest_list.pop()
print (f"Unfortunately {remove_guest}, I can't invite you to dinner")

print(f"\nLucky for me {guest_list[0]}, I still can invite you to dinner")
print(f"Lucky for me {guest_list[1]}, I still can invite you to dinner")

print(len(guest_list))

del guest_list[0]
del guest_list[0]

print(f"\n {guest_list}")


print(len(guest_list))

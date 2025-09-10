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

print(len(guest_list))

gemini = 'smart'
if gemini == 'smart':
    print(f"What about you think about gemini? Of course, very {gemini}")
if gemini != 'idiot':
    print ("He he")

game_show = "Anh Trai Say Hi"
chapter = 1
if chapter < 2:
    print(f"{game_show.lower()} Chapter {chapter}")
if chapter != 2:
    print ("False")

birth_date = 22
if birth_date == 22:
    print ("Date of Birth is 22")
if birth_date != 21:
    print ("Date of Birth is not 21")
if birth_date <= 23:
    print ("Date of Birth is less than 23")
if birth_date >= 20:
    print ("Date of Birth is greater than 20")

age = 23
year_exp = 2

if age < 25 and year_exp in range(1,3):
    print ("Accepted")
if age >= 25 or year_exp in range(2,4):
    print("Not accepted")

fav_fruit = ['apple', 'mango', 'strawberry']
if 'apple' in fav_fruit:
    print("My favorite fruit is apple")
if 'not durian' not in fav_fruit:
    print("My favorite fruit is not durian")
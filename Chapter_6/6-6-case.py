favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }
persons = ['sarah','smith','nelly','edward','athur']
for person in persons:
    if person in favorite_languages:
        print(f"{person.title()}, Thanks for responding!")
    else:
        print (f"{person.title()}, Let take the poll!")

glossaries = {
    'if': 'if statement excute command when conditional test is True',
    'tuple': 'list of immutable',
    'list':'list of data',
    'dictionary': 'object in Javascript',
    'range': 'range begin with first index last second index -1',
    }
for glossary, meaning in glossaries.items():
    print (f"{glossary}: {meaning}")

glossaries['variable'] = 'a named location in memory used to store data that can be changed during program execution.'
glossaries['function'] = 'a block of reusable code that performs a specific task. Functions help organize code and avoid repetition.'
glossaries['loop'] = 'allows you to repeat a block of code multiple times. Python supports for loops and while loops.'
glossaries['listed'] = 'a built-in Python data structure that holds an ordered collection of items, which can be of any type.'
glossaries['conditional statement'] = 'lets you execute certain code only if specific conditions are true.'

for glossary, meaning in glossaries.items():
    print (f"\n{glossary}: {meaning}")



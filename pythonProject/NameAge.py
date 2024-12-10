from datetime import date

current_yr = date.today().year

name = input('What is your name?\n')
age = int(input('How old are you?\n'))
print('\nHello', name + '!', 'You were born in', str(current_yr - age) + '.')

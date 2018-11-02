#This is an exercise in dictionary usage, conditions, and controls.

foodLikes = {'chicken':True, 'kimchi':False, 'avocado':False, 'mashed potato':True}
print('Do I like chicken?')
print(foodLikes['chicken'])
print('If you like kimchi, tell me.')
if 'kimchi' in foodLikes == True:
    print('I like kimchi!')
else:
    print('I do not like kimchi.')
print('Is avocado on the list of foods?')
if 'avocado' in foodLikes:
    print('I have considered avocado')
else:
    print('I have not considered avocado')
print('What about arugula?')
if 'arugula' not in foodLikes:
    print('I have never had arugula')
else:
    print('Yes, I have tried arugula')

print('\nAnd now for something completely different.')
str1 = 'Bob Dole'
str2 = 'Bob Dole'
str3 = str1
print('Are str1 and str2 the same object?')
if str1 is str2:
    print('Yes!')
else:
    print('No.')
print('What about str1 and str3?')
if str1 is str3:
    print('Yes!')
else:
    print('No.')

#But I thought 'is' only returned true if the two variables were pointing to the same object?
#Why, then, does it return true when str1 and str2 have the same value but are two separate objects?

int1 = 1
int2 = 1
int3 = int1

if int1 is int2:
    print('int1 and int2 are the same object')
if int1 == int2:
    print('int1 and int2 have the same value')
if int1 is int3:
    print('int1 and int3 are the same object')

#I have discovered that this is due to 'interning'. 'Folding' is another related thing, but not exemplified here.

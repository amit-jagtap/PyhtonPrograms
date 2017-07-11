s = 'hi'
print('First letter in a String '+s[0])          ## i
print('Length '+str(len(s)))        ## 2
print('Concatinating a String')
print s + ' there'  ## hi there

string1='Hi This Is AMIT'

print('Lower--'+string1.lower())
print('Uper--'+string1.upper())
print('Strip--'+string1.strip('Hi'))

print('Check if string starts with a word or letter')
print(string1)
if string1.startswith('Hi'):
	print('This string starts with Hi')
else:
	print('Wrong string')
print('-----------------------------------------------------')	
print('String='+string1)

id1 = raw_input('Enter a word to find in string: ')
if id1 in string1:
	print('word present in the string')
else:
	print('word not present')
print('-----------------------------------------------------')		
print('')
print('Replacing a Word from a string')
string2='Amit D jagtap'
print('String before replacement:',string2)
replace1=string2.replace('D','Dattatarya')
print('String after replacement:',replace1)
print('-----------------------------------------------------')	
print('-----------------------------------------------------')	
string3='AMIT'
print('Original String--'+string3)
rev1_str = reversed(string3)
print('Reverse of the String--',list(rev1_str))
print('-----------------------------------------------------')	
print('')
print('Check wether the string is Palindrome')
my_str = 'amitima'
print('String--'+my_str)
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")
   
   





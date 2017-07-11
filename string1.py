string=raw_input('enter the string')
if len(string)<2:
   print('')
elif (len(string) == 2):
  print(string * 2)
else:
 print(string[0:2]+string[-2:])

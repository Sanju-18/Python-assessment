#eleminating the equal no.of same alphabets from given names.
lst1 = list(input("Word-1\n"))
lst2 = list(input("Word-2\n"))

i = 0
while i<len(lst1):
  if lst1[i] in lst2:
    lst2.pop(lst2.index(lst1[i]))
    lst1.pop(i)
  else:
    i+=1
    
    
print(''.join(lst1+lst2))

def char_to_text(s):
  s1 = ''
  length = len(s)
  i = 0
  while i<length:
    cnt = 0
    s1+=s[i]
    if s.count(s[i])>1:
      j = i+1
      while j<length:
        if s[i]==s[j]:
          cnt+=1
          j+=1
        else:
          break
    if cnt!=0:
      s1+=str(cnt+1)
      i+=cnt+1
    else:
      i+=1
  return s1
      

value = input("Enter the value \n").split(' ')
new_value = []
for i in value:
  new_value.append(char_to_text(i))
print(new_value)
s ="leet code"
index = -1
fnc = ""
 
for i in s:
    if s.count(i) == 1:
        fnc += i
        break
    else:
        index += 1
if index == len(s)-1 :
    print(-1)
else:
    print(s.index(fnc))
 


S = ".X.XX..X"

newList = []
count = 0
for i in range(0, len(S), 3):
    
    newList.append(S[i : i + 3])
    
    if "X" in S[i : i + 3]:
        count += 1
    else:
        pass



print(newList)
print(count)



A = [-1, -2, 1, 3, 6]

def solution(A):
    
    A.sort()
    x = max(A)
    if x <= 0:
        return 1
    else:
        for y in A:
            if y <= 0:
                pass
            else:
                z = y + 1
                if z not in A:
                    return z
                else:
                    pass

print(solution(A))
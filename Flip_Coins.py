

# PROBLEM NOT SOLVED



a = [1, 0, 1, 0, 1, 1]
b = [1, 1, 0, 1, 1]
c = [0, 1, 0]
d = [0, 1, 1, 0]



def solution(data):

    if data[0] == 1 and data[1] == 0:
        x = 'oneZero'
    
    elif data[0] == 0 and data [1] == 1:
        x = 'zeroOne'

    elif data[0] == 1 and data [1] == 1:
        x = 'oneOne'

    else: 
        x = 'zeroZero'
    
    
    
    count = 0

    for index in range(0, len(data) - 1, 2):
        print(index)
        
        if index >= len(data) - 1:
            break

        elif data[index] != first or data[ index + 1] != second:
            count = 1
    
    return count


print(solution(a), 1)
print(solution(b), 2)
print(solution(c), 0)
print(solution(d), 2)


# def valley(data): #valley list
#     valley = []
    
#     for index in range(len(data)):
#         if index == 0: # skip first item on the list
#             index = index + 1 
#         elif data[index] < (data[index - 1]) and data[index] < data[index + 1]:
#             #if item is smaller than item location -1 and item location +1
#             valley.append(index)
         
#     return valley

# def peak_and_valley(data):
#     peak_and_valley = []

#     for index in range(len(data) - 1): #add -1 to avoid end of list error
#         if (data[index] > (data[index - 1]) and data[index] > data[index + 1]) or (data[index] < (data[index - 1]) and data[index] < data[index + 1]): 
#             # if item is bigger than item location -1 and item location +1
#             peak_and_valley.append(index)
#     peak_and_valley.pop(0)
#     return peak_and_valley



# print(f'''
# Peak index/es: 
# {peak(data)}

# Valley index/es: 
# {valley(data)}

# Peak and Valley index/es: 
# {peak_and_valley(data)} 
# ''')
    
    


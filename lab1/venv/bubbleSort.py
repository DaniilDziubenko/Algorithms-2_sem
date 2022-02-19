import random

def sort_bubble(arr):
    numCompare = 0
    numSwap = 0
    flag = True
    i = 0
    while flag and i < len(arr) - 1:
        flag = False
        for j in range(len(arr) - i - 1):
            numCompare += 1
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                flag = True
                numSwap += 1
        i += 1
    print("Number of compares:", numCompare)
    print("Number of swaps:", numSwap)
    return arr

n = 10
random_arr = []

for i in range(n):
    random_arr.append(i+1)

# while n>0:
#     random_arr.append(n)
#     n -= 1

# random_arr = random.sample(range(1, n+1), n)
print('Basic array:', random_arr)

sorted_arr = sort_bubble(random_arr)
print('New array:', sorted_arr)
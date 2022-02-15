import random

def sort_bubble(arr):
    numCompare = 0
    numSwap = 0
    for i in range(len(arr)):
        flag = True
        for j in range(len(arr) - i -1):
            numCompare += 1
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                flag = False
                numSwap += 1
        if flag:
            print("Array is already sorted!")
            break
    print("Number of compares:", numCompare)
    print("Number of swaps:", numSwap)
    return arr

n = 50000
random_arr = []

while n>0:
    random_arr.append(n)
    n -= 1

# random_arr = random.sample(range(1, n+1), n)
print('Basic array:', random_arr)

sorted_arr = sort_bubble(random_arr)
print('New array:', sorted_arr)
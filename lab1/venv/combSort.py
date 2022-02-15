import random

def sort_comb(arr):
    numCompare = 0
    numSwap = 0
    step = len(arr) - 1
    while step >= 1:
        for i in range(len(arr) - step):
            numCompare += 1
            if arr[i] > arr[i + step]:
                b = arr[i]
                arr[i] = arr[i+step]
                arr[i+step] = b
                numSwap += 1
        step = int(step / 1.247)
    print("Number of compares:", numCompare)
    print("Number of swaps:", numSwap)
    return arr

n = 1000

random_arr = random.sample(range(1, n+1), n)
print('Basic array:', random_arr)

sorted_arr = sort_comb(random_arr)
print('New array:', sorted_arr)
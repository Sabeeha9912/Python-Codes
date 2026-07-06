# selection sort
def selection_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):    # smallest element in remaining lis
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:    # swap 
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
        print(f"Iteration {i + 1}: {arr}")
    print("\nTotal number of swaps:", swaps)
numbers = [64, 25, 12, 22, 11]  #e.g
selection_sort(numbers)

# insertion sort
def insertion_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        arr[j + 1] = key
        print(f"Iteration {i}: {arr}")
    print("\nTotal number of swaps:", swaps)
numbers = [64, 34, 25, 12, 22, 11]  # e.g
insertion_sort(numbers)

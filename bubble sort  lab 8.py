# bubble sort
def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n - 1):
        print(f"\nIteration {i + 1}:")
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]   # swap
                swaps += 1
        print(arr)   # list after each iteration
    print("\nTotal number of swaps:", swaps)
numbers = [64, 34, 25, 12, 22, 11, 90]  # e.g
bubble_sort(numbers)

# Binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    searches = 0
    while low <= high:
        searches += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            print(f"Element {target} found at index {mid}")
            print("Total number of searches:", searches)
            return
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print(f"Element {target} not found")
    print("Total number of searches:", searches)
numbers = [10, 20, 30, 40, 50, 60, 70, 80]  #e.g
search_element = 50
binary_search(numbers, search_element)

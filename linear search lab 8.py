# linear search
def linear_search(arr, target):
    found = False
    for index in range(len(arr)):
        if arr[index] == target:
            print(f"Element {target} found at index {index}")
            found = True
            break
    if not found:
        print(f"Element {target} not found in the list")
numbers = [10, 25, 30, 45, 60, 75]  #e.g
search_element = 45
linear_search(numbers, search_element)

# Generate random list and sum 
import random
numbers = [random.randint(0, 1000) for _ in range(10)]
print("Random numbers:", numbers)
def recursive_sum(lst, index=0):    #Recursive function to add all elements in the list
    if index == len(lst):   # base case
        return 0
    return lst[index] + recursive_sum(lst, index + 1)
total = recursive_sum(numbers)  #sum
print("Sum using recursion:", total)


# =========================================================================
# 1. BASIC LIST OPERATIONS
# =========================================================================
def demonstrate_basic_list():
    print("--- 1. Basic List Operations ---")
    my_list = [1, 2, 3, "4", 5.0]
    print("Original List:", my_list)
    print("Length:", len(my_list)) 
    print("Type:", type(my_list))
    print("Element at index 0:", my_list[0]) 
    
    my_list.append(5)
    print("After Append(5):", my_list)
    print("New Length:", len(my_list))
    print("Dynamic math indexing:", my_list[len(my_list) - 4]) 
    print("-" * 40 + "\n")


# =========================================================================
# 2. LIST SLICING (FRUITS)
# =========================================================================
def demonstrate_slicing():
    print("--- 2. List Slicing Demo ---")
    fruits = ["apple", "banana", "orange", "grapes", "pine apple"]
    print("fruits[1:5]:", fruits[1:5])
    print("fruits[-6:-2]:", fruits[-6:-2])
    print("fruits[-2:-1:2]:", fruits[-2:-1:2])
    print("-" * 40 + "\n")


# =========================================================================
# 3. CHANGING VALUES IN A NESTED LIST
# =========================================================================
def demonstrate_value_modifications():
    print("--- 3. Modifying Nested Items ---")
    L = ["a", ["bb", "cc"], "d"]
    print("Original L:", L)
    
    L[1][1] = 0
    print("After L[1][1] = 0:", L)
    
    L[1][-2] = 8
    print("After L[1][-2] = 8:", L)
    print("-" * 40 + "\n")


# =========================================================================
# 4. SORTING, REVERSING & JUMP SLICING
# =========================================================================
def demonstrate_sorting_and_advanced_slicing():
    print("--- 4. Methods & Advanced Slicing ---")
    c = [1, 3, 2, 7, 5]
    
    c.sort()
    print("Sorted 'c':", c)
    
    c.reverse()
    print("Reversed 'c':", c)
    
    print("Count of 3 in c[1:4]:", c[1:4].count(3)) 
    print("Slicing c[1:4]:", c[1:4])
    print("Empty slice c[4:1]:", c[4:1]) 
    print("Full copy c[::]:", c[::])  
    print("Full copy c[:]:", c[:])   
    print("Reverse slice c[::-1]:", c[::-1]) 
    print("Reverse step-2 c[::-2]:", c[::-2])  
    print("Negative bound slice c[-5:-1:2]:", c[-5:-1:2])
    print("-" * 40 + "\n")


# =========================================================================
# 5. DYNAMIC USER INPUT & DUPLICATE REMOVAL
# =========================================================================
def demonstrate_user_input():
    print("--- 5. List Inputs & Deduplication ---")
    print("Example format: 1, 2, 2, 3, 4, 4, 5")
    lists = input("Enter numbers separated by commas: ")
    
    try:
        a = [int(x.strip()) for x in lists.split(",")]
        # Removes repeating values while preserving order
        new_string = list(dict.fromkeys(a)) 
        print("Deduplicated output list:", new_string)
    except ValueError:
        print("Error: Please make sure you enter numbers only separated by commas!")
    print("-" * 40 + "\n")


# =========================================================================
# 6. EXTENDING LISTS & OPERATOR CONCATENATION
# =========================================================================
def demonstrate_extensions():
    print("--- 6. Extending Lists ---")
    l = [-2, 5, 8, 9, 7, -8, -222, 444, 0, -2, 5, 5]
    m = ["hello", "UET"]
    
    l.extend(m)
    print("Extended 'l':", l)
    
    m = m + [8]  
    print("Concatenated 'm':", m)
    print("-" * 40 + "\n")


# =========================================================================
# 7. DEEPLY NESTED LIST MANAGEMENT
# =========================================================================
def demonstrate_deeply_nested_lists():
    print("--- 7. Deeply Nested Structures ---")
    a = [1, 2, [3, 4, [5, 6], 7], 8] 
    print("Element a[3]:", a[3])
    print("Deep element a[2][2][0]:", a[2][2][0])
    
    a[2][2][1] = 0
    print("After modification:", a)
    
    a[2][2].append("x")
    print("After deep append:", a)
    print("-" * 40 + "\n")


# =========================================================================
# 8. FRUITS LIST CONDITIONAL LOGIC & SEARCH INDEXING
# =========================================================================
def demonstrate_conditionals_and_indexing():
    print("--- 8. Conditionals & Index Search ---")
    fruits = ["Apple", "banana", "strawbery", "grapes", "melon", "watermwlon", "orange"]
    print("Negative bound slice:", fruits[-5:-2])
    
    if "banana" in fruits:
        print("Result: Yes, 'banana' is in the fruits list!")
        
    fruits.sort()
    print("Alphabetically sorted fruits:", fruits)
    
    # Index lookups on target items
    l = [-2, 5, 8, 9, 7, -8, -222, 444, 0, -2, 5, 5]
    print("First index position of 5:", l.index(5))
    print("Index position of 5 within range l[5:11]:", l[5:11].index(5))
    print("-" * 40 + "\n")


# =========================================================================
# CENTRAL MASTER EXECUTION DRIVER
# =========================================================================
if __name__ == "__main__":
    # Running all function execution blocks sequentially
    demonstrate_basic_list()
    demonstrate_slicing()
    demonstrate_value_modifications()
    demonstrate_sorting_and_advanced_slicing()
    demonstrate_user_input()  # Will request a quick input string in console
    demonstrate_extensions()
    demonstrate_deeply_nested_lists()
    demonstrate_conditionals_and_indexing()
    
    print("All tasks finished running completely without conflicts!")

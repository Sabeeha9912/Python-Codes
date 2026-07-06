# =========================================================================
# 1. SET BASICS, SYNTAX & DATA TYPES
# =========================================================================
def demonstrate_set_basics():
    print("--- 1. Set Basics & Initialization ---")
    a = {1, 3, 5}
    print("Original set 'a':", a)
    print("Type of 'a':", type(a))
    print("Length of 'a':", len(a))
    
    # Empty set syntax declaration (Using {} creates a dictionary)
    emptyset = set() 
    print("Type of empty set variable:", type(emptyset))
    print("-" * 40 + "\n")


# =========================================================================
# 2. ADDING, REMOVING, CLEARING & POPPING
# =========================================================================
def demonstrate_set_mutations():
    print("--- 2. Adding, Removing, & Popping Elements ---")
    emptyset = set()
    
    # Adding various immutable types
    emptyset.add(1)
    emptyset.add(2)
    emptyset.add("1,2,3")   # Strings are allowed
    emptyset.add((1, 2, 3)) # Tuples are allowed (dicts/lists are not allowed as elements)
    print("Set after adds:", emptyset)
    
    # Removing a specific value
    emptyset.remove(1)
    print("Set after removing '1':", emptyset)
    
    # Clearing the set entirely
    emptyset.clear()
    print("Set after clear():", emptyset)
    print("Length after clear():", len(emptyset))
    
    # Popping an arbitrary random element
    word_set = {"reg.no", "name", "city", "home"}
    popped_val = word_set.pop()
    print(f"Popped value: '{popped_val}' | Remaining set:", word_set)
    print("-" * 40 + "\n")


# =========================================================================
# 3. CORE SET OPERATIONS (UNION & INTERSECTION)
# =========================================================================
def demonstrate_set_operations():
    print("--- 3. Core Set Mathematics (Union & Intersection) ---")
    s = {1, 3, 5}
    t = {2, 4, 6, 5}
    print("Set s:", s)
    print("Set t:", t)
    print("Union (s ∪ t):", s.union(t))
    print("Intersection (s ∩ t):", s.intersection(t))
    print("-" * 40 + "\n")


# =========================================================================
# 4. LAB PRACTICE (CASTING, DISCARD, & UPDATE)
# =========================================================================
def demonstrate_lab_exercises():
    print("--- 4. Lab Practices & Built-In Methods ---")
    s = {1, 3.6, "Uet"}
    s1 = set([44.5, "UET", 7, 7, 7]) # Deduplicates list entries automatically
    print("Set s:", s)
    print("Set s1 (Casted from list):", s1)
    print("Type of s:", type(s))
    print("Type of s1:", type(s1))
    
    s.add("CYS")
    print("s after adding 'CYS':", s)
    
    s1.remove(7)
    print("s1 after removing 7:", s1)
    
    s.discard(44.5) # Discard does not raise an error if item isn't present
    print("s after discarding 44.5:", s)
    
    s.update(s1)
    print("s after updating with s1 elements:", s)
    print("-" * 40 + "\n")


# =========================================================================
# 5. USER INPUT FOR SET COMPREHENSION
# =========================================================================
def demonstrate_set_input():
    print("--- 5. Dynamic Set Comprehension Input ---")
    print("Example format: 1, 2, 3, 4, 5")
    user_string = input("Enter any numbers separated by commas: ")
    
    try:
        b = {int(x.strip()) for x in user_string.split(",")}
        print("Generated Set from Input:", b)
    except ValueError:
        print("Error: Please provide integer values separated only by commas.")
    print("-" * 40 + "\n")


# =========================================================================
# 6. ADVANCED STRING SET METHODS
# =========================================================================
def demonstrate_string_set_methods():
    print("--- 6. String Set Methods & Set Differences ---")
    s1 = {"zeerak", "ahmad", "ali"}
    s2 = {"Fatima", "maryam", "amina", "ahmad"}
    
    i = s1.intersection(s2)
    print("INTERSECTION IS:", i)
    
    u = s1.union(s2)
    print("UNION IS:", u)
    
    print("Difference in sets (s1 - s2):", s1.difference(s2))
    
    # s2.update(s1) performs an in-place modification and returns None. 
    # To view the changes, we execute the operation first, then print s2.
    s2.update(s1)
    print("Updated s2 (after adding all s1 entries):", s2)
    print("-" * 40 + "\n")


# =========================================================================
# CENTRAL MASTER EXECUTION DRIVER
# =========================================================================
if __name__ == "__main__":
    demonstrate_set_basics()
    demonstrate_set_mutations()
    demonstrate_set_operations()
    demonstrate_lab_exercises()
    demonstrate_set_input()  # Prompts for inputs in console terminal window
    demonstrate_string_set_methods()
    
    
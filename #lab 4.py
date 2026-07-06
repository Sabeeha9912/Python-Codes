# =========================================================================
# LAB 4: LIST DATA TYPES & CALCULATED INDEXING
# =========================================================================
def demonstrate_lab_4_lists():
    print("--- Lab 4: List Basics & Index Fixes ---")
    my_list = [1, 2, 3, "4", 5.0]
    print("Original List:", my_list)
    print("Type of Collection:", type(my_list))
    print("Value at index 0:", my_list[0])  # 0 is the starting index
    
    # Adding an item to the end of the list
    my_list.append(5)
    print("After appending 5:", my_list)
    
    # FIXING THE SYNTAX: Changed round brackets () to square brackets []
    # len(my_list) is 6. So, 6 - 4 = 2.
    # my_list[2] points directly to the integer 3.
    calculated_index = len(my_list) - 4
    print(f"Calculated element at index [{calculated_index}]:", my_list[calculated_index])
    print("-" * 40 + "\n")


# =========================================================================
# CENTRAL MASTER EXECUTION DRIVER
# =========================================================================
if __name__ == "__main__":
    demonstrate_lab_4_lists()
    
    print("Lab 4 block executed completely without errors!")
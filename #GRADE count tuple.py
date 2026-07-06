# =========================================================================
# 1. COUNTING SPECIFIC GRADES
# =========================================================================
def demonstrate_grade_counting():
    print("--- 1. Grade Counting ---")
    a = ["C", "D", "B", "B", "A", "A"]
    print("Grade List:", a)
    print("Number of 'A' grades:", a.count("A"))
    print("-" * 40 + "\n")


# =========================================================================
# 2. ALPHABETICAL GRADE SORTING (ASCENDING & DESCENDING)
# =========================================================================
def demonstrate_grade_sorting():
    print("--- 2. Grade Sorting ---")
    a = ['C', 'D', 'A', 'A', 'B', 'B', 'A']
    print("Original Unsorted Grades:", a)
    
    # Sorting in normal ascending order (A, B, C, D...)
    a.sort()
    print("Sorted Ascending (A -> D):", a)
    
    # Sorting in reverse descending order (D, C, B, A...)
    a.sort(reverse=True)
    print("Sorted Descending (D -> A):", a)
    print("-" * 40 + "\n")


# =========================================================================
# CENTRAL MASTER EXECUTION DRIVER
# =========================================================================
if __name__ == "__main__":
    demonstrate_grade_counting()
    demonstrate_grade_sorting()
    
    print("All grade manipulation blocks executed perfectly!")
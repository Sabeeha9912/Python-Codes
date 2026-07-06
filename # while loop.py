# =========================================================================
# 1. REVERSE COUNTDOWN (100 TO 1)
# =========================================================================
def demonstrate_countdown():
    print("--- 1. While Loop Countdown (100 to 1) ---")
    a = 100
    while a >= 1:
        print(a, end=" ")  # Prints on the same line to keep console clean
        a = a - 1
    print("\n" + "-" * 40 + "\n")


# =========================================================================
# 2. MULTIPLICATION TABLE (TABLE OF 3)
# =========================================================================
def demonstrate_multiplication_table():
    print("--- 2. Multiplication Table (Table of 3) ---")
    n = 3
    i = 1
    while i <= 10:
        a = n * i
        print(f"{n} * {i} = {a}")
        i += 1
    print("-" * 40 + "\n")


# =========================================================================
# 3. TRAVERSING A LIST VIA INDEX
# =========================================================================
def demonstrate_list_traversal():
    print("--- 3. Printing List Items using While Loop ---")
    n = [1, 4, 8, 10, 15, 17]
    idx = 0 
    while idx < len(n):
        print(f"Index {idx}: {n[idx]}")
        idx = idx + 1
    print("-" * 40 + "\n")


# =========================================================================
# 4. BREAK STATEMENT DEMO
# =========================================================================
def demonstrate_break():
    print("--- 4. Break Statement Demo (Stops loop at 7) ---")
    a = 5
    while a <= 10:
        print(a)
        if a == 7:  # After 7 nothing will print as break terminates the loop
            break
        a += 1
    print("Loop broken successfully!")
    print("-" * 40 + "\n")


# =========================================================================
# 5. CONTINUE STATEMENT DEMO (FIXED INFINITE LOOP)
# =========================================================================
def demonstrate_continue():
    print("--- 5. Continue Statement Demo (Skips 7) ---")
    a = 5
    while a <= 10:
        if a == 7:
            a += 1    # CRITICAL FIX: Increment before continuing to avoid an infinite loop!
            continue  # Skips the print statement for 7
        print(a)
        a += 1
    print("-" * 40 + "\n")


# =========================================================================
# 6. SUM OF FIRST N NATURAL NUMBERS (USER INPUT)
# =========================================================================
def demonstrate_natural_sum():
    print("--- 6. Sum of First N Natural Numbers ---")
    try:
        n = int(input("Enter any range limit number: "))
        i = 1
        total = 0
        while i <= n:
            total = total + i
            i = i + 1
        print(f"The total sum from 1 to {n} is: {total}")
    except ValueError:
        print("Error: Please enter a valid integer number!")
    print("-" * 40 + "\n")


# =========================================================================
# CENTRAL MASTER EXECUTION DRIVER
# =========================================================================
if __name__ == "__main__":
    demonstrate_countdown()
    demonstrate_multiplication_table()
    demonstrate_list_traversal()
    demonstrate_break()
    demonstrate_continue()
    demonstrate_natural_sum()  # Prompts for numerical input boundary limits
    
    print("All while loop control blocks finished execution successfully!")
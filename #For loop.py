# =========================================================================
# 1. LIST TRAVERSAL (COLORS)
# =========================================================================
def demonstrate_colors_loop():
    print("--- 1. For Loop over Colors List ---")
    colors = ["black", "blue", "pink", "red", "green", "brown"]
    
    # Iterates and prints each single element one by one
    for value in colors:
        print(value)
    print("-" * 40 + "\n")


# =========================================================================
# 2. LIST TRAVERSAL (NUMBERS)
# =========================================================================
def demonstrate_numbers_loop():
    print("--- 2. For Loop over Numbers List ---")
    a = [1, 3, 5, 7, 8, 9]
    for elm in a:
        print(elm)
    print("-" * 40 + "\n")


# =========================================================================
# 3. FACTORIAL VIA RANGE LOOP (USER INPUT)
# =========================================================================
def demonstrate_factorial_loop():
    print("--- 3. Iterative Factorial using range() ---")
    try:
        a = int(input("Enter any positive integer: "))
        fact = 1
        
        # range(1, a+1) runs from 1 up to 'a'
        for i in range(1, a + 1):
            fact = fact * i
            
        print(f"The factorial result is: {fact}")
    except ValueError:
        print("Error: Please provide a valid integer value.")
    print("-" * 40 + "\n")


# =========================================================================
# CENTRAL MASTER EXECUTION DRIVER
# =========================================================================
if __name__ == "__main__":
    demonstrate_colors_loop()
    demonstrate_numbers_loop()
    demonstrate_factorial_loop()  # Will ask for a number in the console window
    
    print("All Python for loop blocks completed execution!")
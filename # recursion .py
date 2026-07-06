# =========================================================================
# 1. BASIC RECURSION (COUNTDOWN)
# =========================================================================
def demonstrate_countdown(a):
    if a == 0:
        return
    print(a)
    demonstrate_countdown(a - 1)


# =========================================================================
# 2. FACTORIAL USING RECURSION
# =========================================================================
def calculate_factorial(n):
    if n == 1 or n == 0:
        return 1
    return calculate_factorial(n - 1) * n


# =========================================================================
# 3. SUM OF NATURAL NUMBERS USING RECURSION
# =========================================================================
def calculate_sum(n):
    if n == 0:
        return 0
    return calculate_sum(n - 1) + n


# =========================================================================
# CENTRAL MASTER EXECUTION DRIVER
# =========================================================================
if __name__ == "__main__":
    
    print("--- 1. Recursive Countdown Demo (show 5 to 1) ---")
    demonstrate_countdown(5)
    print("-" * 40 + "\n")
    
    print("--- 2. Recursive Factorial Demo (fact of 4) ---")
    factorial_result = calculate_factorial(4)
    print(f"Factorial Result: {factorial_result}")
    print("-" * 40 + "\n")
    
    print("--- 3. Recursive Sum Demo (sum up to 5) ---")
    sum_result = calculate_sum(5)
    print(f"Sum Result: {sum_result}")
    print("-" * 40 + "\n")
    
    print("All recursive tasks executed successfully!")
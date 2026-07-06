# =========================================================================
# 1. RECURSIVE FORWARD PRINTING (1 TO N)
# =========================================================================
def demonstrate_forward_print(n):
    if n == 0:
        return
    else:
        # Recursive call happens BEFORE the print statement.
        # This pauses the printing stack until it reaches 0, 
        # meaning numbers print in ascending order (1 to 5) as the stack unwinds.
        demonstrate_forward_print(n - 1)
    print(n)


# =========================================================================
# 2. RECURSIVE SUMMATION (1 TO N)
# =========================================================================
def calculate_recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + calculate_recursive_sum(n - 1)


# =========================================================================
# 3. OPTIMIZED FIBONACCI WITH MEMOIZATION (DYNAMIC PROGRAMMING)
# =========================================================================
def calculate_fibonacci_memo(n, memo=None):
    # Initialize a fresh dictionary locally to prevent sharing state across separate function calls
    if memo is None:
        memo = {}
        
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
        
    memo[n] = calculate_fibonacci_memo(n - 1, memo) + calculate_fibonacci_memo(n - 2, memo)
    return memo[n]


# =========================================================================
# 4. RECURSIVE SUM OF DIGITS (COMPLETED)
# =========================================================================
def calculate_sum_of_digits(n):
    # Base Case
    if n == 0:
        return 0
    # Modulo (%) gets the rightmost digit, Integer Division (//) slices it away
    return (n % 10) + calculate_sum_of_digits(n // 10)


# =========================================================================
# CENTRAL MASTER EXECUTION DRIVER
# =========================================================================
if __name__ == "__main__":
    
    print("--- 1. Recursive Forward Printing (1 to 5) ---")
    demonstrate_forward_print(5)
    print("-" * 40 + "\n")
    
    print("--- 2. Recursive Summation Result (Up to 5) ---")
    total_sum = calculate_recursive_sum(5)
    print(f"Sum total: {total_sum}")
    print("-" * 40 + "\n")
    
    print("--- 3. Memoized Fibonacci Calculation (Element 7) ---")
    fib_value = calculate_fibonacci_memo(7)
    print(f"Fibonacci value at index 7: {fib_value}")
    print("-" * 40 + "\n")
    
    print("--- 4. Recursive Digit Summation (Example: 12345) ---")
    digit_test_val = 12345
    digit_sum = calculate_sum_of_digits(digit_test_val)
    print(f"The sum of all individual digits in {digit_test_val} is: {digit_sum}")
    print("-" * 40 + "\n")
    
    print("All advanced recursive algorithm modules completed successfully!")
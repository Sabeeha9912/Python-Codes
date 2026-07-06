import math
import string
import secrets

# =========================================================================
# 1. GEOMETRY & MATHEMATICAL TRIGNOMETRY
# =========================================================================
def demonstrate_geometry_and_math():
    print("--- 1. Geometry & Trigonometry ---")
    try:
        r = int(input("Enter any radius integer for a sphere: "))
        print("Radius:", r)
        v = (4 / 3) * 3.147 * r**3
        print("Volume:", v)
    except ValueError:
        print("Invalid radius input skipped.")

    x = 10
    angle = 30
    a = math.cos(angle) * math.sqrt(x**2)
    print("Trigonometric custom result (a):", a)
    print("-" * 40 + "\n")


# =========================================================================
# 2. BASIC STRINGS, CONDITIONAL LOGIC & PARSING
# =========================================================================
def demonstrate_conditionals_and_vowels():
    print("--- 2. Conditionals, Vowels, & Loops ---")
    try:
        a = int(input("Enter any number to check parity: "))
        if a % 2 == 0:
            print("Even")
        else:
            print("Not even")
    except ValueError:
        print("Invalid parity input.")

    text = input("Enter any word to repeat: ")
    try:
        n = int(input("Enter multiplication scale index: "))
        print(text * n)
    except ValueError:
        print("Invalid iteration counter.")

    word_sample = "statement"
    sum_vowels = 0
    vowels = "aeiou"
    for ch in word_sample:
        if ch in vowels:
            sum_vowels += 1
    print(f"Number of vowels in '{word_sample}':", sum_vowels)
    print("-" * 40 + "\n")


# =========================================================================
# 3. ALIASING VS COPYING & SECURITY LOOPS
# =========================================================================
def demonstrate_aliasing_and_security():
    print("--- 3. Shallow Aliasing vs Password Security Loops ---")
    # Aliasing demo (Modifying values step-by-step)
    a = 1
    b = a
    print("Initial alias mapping b:", b)
    b = 5
    a = b
    print("Re-assigned reference state a:", a)

    password = "secret"
    max_try = 3
    trys = 0
    while trys < max_try:
        user_input = input("Enter password: ")
        trys += 1
        if user_input == password:
            print("Access granted")
            break
        else:
            print("Error. Try again")
    if trys == max_try and user_input != password:
        print("You have exceeded the limit.")
    print("-" * 40 + "\n")


# =========================================================================
# 4. PATTERN GENERATOR BLOCKS & STRING SLICING
# =========================================================================
def demonstrate_patterns_and_ascii():
    print("--- 4. Pattern Generators & ASCII Slicing ---")
    try:
        limit = int(input("Enter limit integer for natural sum loop: "))
        total_sum = 0
        for i in range(limit + 1):
            total_sum = limit + i
        print("Your final tracking sum is:", total_sum)
    except ValueError:
        print("Invalid numerical boundary range.")

    word_in = input("Enter a word for ordinal ASCII conversions: ")
    for character in word_in:
        print(f"{character} ---> {ord(character)}")

    print("\n[Pattern 1 (Numbers)]")
    n = 5
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()

    print("\n[Pattern 2 (Nested Words)]")
    word_py = "python"
    for i in range(len(word_py)):
        for j in range(i + 1):
            print(word_py[j], end="")
        print()

    print("\n[Pattern 3 (String Slice Steps)]")
    word_cap = "Python"
    for i in range(0, len(word_cap) + 1, 1):
        print(word_cap[:i])
    print("-" * 40 + "\n")


# =========================================================================
# 5. ADVANCED NESTED LOOPS & UTILITIES
# =========================================================================
def demonstrate_character_analytics():
    print("--- 5. Character Analytics & Asterisk Triangles ---")
    sentence = input("Enter a sentence for detailed breakdown: ")
    num_vowels = 0
    num_constant = 0
    vowels = "aeiouAEIOU"
    for character in sentence:
        if character.isalpha():  # Filters spaces and syntax punctuation
            if character in vowels:
                num_vowels += 1
            else:
                num_constant += 1
    print("No. of vowels are:", num_vowels)
    print("No. of consonants are:", num_constant)

    print("\n[Bi-directional Asterisk Triangle]")
    for i in range(1, 5):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
    for i in range(3, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
    print("-" * 40 + "\n")


# =========================================================================
# 6. RANDOM GENERATORS & COMBINATORICS
# =========================================================================
def generate_password_utility():
    print("--- 6. Cryptographically Secure Password Generator ---")
    try:
        length = int(input("Enter desired password length: "))
        upper_case = input("Include upper case letters? (y/n): ").lower() == 'y'
        lower_case = input("Include lower case letters? (y/n): ").lower() == 'y'
        digits = input("Include numerical digits? (y/n): ").lower() == 'y'
        special_symbol = input("Include special symbols? (y/n): ").lower() == 'y'
        
        character = ''
        if upper_case: character += string.ascii_uppercase
        if lower_case: character += string.ascii_lowercase
        if digits:     character += string.digits
        if special_symbol: character += string.punctuation
        
        if not character:
            print("Error: You must select at least a single dataset layer type.")
            return
            
        password = ''.join(secrets.choice(character) for _ in range(length))
        print("Generated password is:", password)
    except ValueError:
        print("Invalid generation parameters.")
    print("-" * 40 + "\n")


# =========================================================================
# 7. PRIME RANGES & STATISTICAL OPERATIONS
# =========================================================================
def demonstrate_primes_and_combinatorics():
    print("--- 7. Prime Number Searching & Combinatorics ---")
    try:
        starting = int(input("Enter starting lookup search value: "))
        ending = int(input("Enter ending lookup search values: "))
        print(f"Prime numbers between {starting} and {ending} are:")
        prime_no = []
        
        for n in range(starting, ending + 1):
            if n > 1:
                for i in range(2, int(math.sqrt(n)) + 1):
                    if n % i == 0:
                        break
                else:
                    print(n, end=" ")
                    prime_no.append(n)
        print(f"\nPrime total sum accumulation: {sum(prime_no)}")
    except ValueError:
        print("Invalid prime bound integers parsed.")

    print("\n[Combinations & Permutations]")
    try:
        n_val = int(input("Enter pooling context item count (n): "))
        r_val = int(input("Enter target arrangement subset size (r): "))
        
        if n_val >= r_val:
            c = math.factorial(n_val) // (math.factorial(r_val) * math.factorial(n_val - r_val))
            p = math.factorial(n_val) // math.factorial(n_val - r_val)
            print("Combination C(n,r) is:", c)
            print("Permutation P(n,r) is:", p)
        else:
            print("Error: Size n must be greater or equal to target constraint r.")
    except ValueError:
        print("Error processing algebraic inputs.")
    print("-" * 40 + "\n")


# =========================================================================
# 8. DECIMAL TO BINARY CONVERSIONS & SETS LABS
# =========================================================================
def demonstrate_binary_and_sets():
    print("--- 8. Conversions, Single Primes & Collections ---")
    try:
        a = int(input("Enter a decimal base-10 number: "))
        print(f"Binary implementation mapping of {a}: {bin(a)}")
        
        # Single Prime Checker Module
        if a > 1:
            for i in range(2, int(math.sqrt(a)) + 1):
                if a % i == 0:
                    print(f"The number {a} is NOT a prime element.")
                    break
            else:
                print(f"The number {a} is a Prime element.")
        else:
            print(f"The number {a} is non-prime by foundational bounds.")
    except ValueError:
        print("Invalid translation sequence data parsing.")

    s = {1, 3.6, "Uet"}
    s1 = set([44.5, "UET", 7])
    print("\nSet s:", s)
    print("Set s1:", s1)
    print("-" * 40 + "\n")


# =========================================================================
# 9. COMPREHENSIONS & TRANSPOSE MATRIX ARRAY MATHEMATICS
# =========================================================================
def demonstrate_matrix_and_comprehensions():
    print("--- 9. List Comprehensions & 3x3 Matrix Transpositions ---")
    lst = [i for i in range(5)]
    print("Basic comprehension [0-4]:", lst)
    
    squared_evens = [i*i for i in range(10) if i % 2 == 0]
    print("Squared evens sequence list:", squared_evens)

    # 3x3 Matrix Routine
    matrix = []
    print("\nEnter 3 elements for each row of your 3x3 Matrix:")
    try:
        for i in range(3):
            row = list(map(int, input(f"Enter row elements {i+1} (space separated): ").split()))
            if len(row) != 3:
                print("Error: Row must contain exactly 3 numbers. Appending zeros.")
                row = [0, 0, 0]
            matrix.append(row)
            
        print("\nOriginal 3x3 Matrix Layout:")
        for row in matrix:
            print(row)

        # Transposition Logic: Flips rows to columns
        transpose = [[matrix[j][i] for j in range(3)] for i in range(3)]
        
        print("\nTranspose Matrix Layout Result:")
        for row in transpose:
            print(row)
    except Exception as e:
        print("Matrix configuration reading aborted:", e)
    print("-" * 40 + "\n")


# =========================================================================
# 10. ACADEMIC GRADE ESTIMATIONS (GPA CALCULATOR)
# =========================================================================
def calculate_gpa():
    print("--- 10. Academic Semester GPA Calculator ---")
    try:
        total_grade_points = 0.0
        total_credit_hours = 0.0
        subject = int(input("Enter number of subjects: "))
        
        for i in range(1, subject + 1):
            print(f"Subject {i}:")
            grade_points = float(input("  Enter grade points: "))
            credit_hours = float(input("  Enter credit hours: "))
            total_grade_points += grade_points * credit_hours
            total_credit_hours += credit_hours
            
        if total_credit_hours > 0:
            gpa = total_grade_points / total_credit_hours
            print(f"\nCalculated Semester GPA metric output: {gpa:.2f}")
        else:
            print("Credit distribution balance null state error.")
    except ValueError:
        print("Invalid academic points evaluation sequence entry.")
    print("-" * 40 + "\n")


# =========================================================================
# 11. RECURSIVE ALGORITHMS (FIBONACCI SEQUENCING)
# =========================================================================
def demonstrate_recursion_fibonacci():
    print("--- 11. Recursive Fibonacci Generator Sequence ---")
    def fib(n):
        if n <= 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print("First 10 indices of the Fibonacci sequence layout:")
    for i in range(10):
        print(fib(i), end=" ")
    print("\n" + "-" * 40 + "\n")


# =========================================================================
# 12. ADVANCED LAB METHOD ARCHITECTURES
# =========================================================================
def demonstrate_lambda_and_args():
    print("--- 12. Advanced Keyword Args (**kwargs) & Lambda Evaluation ---")
    
    # Pack parameters into dictionaries via **kwargs
    def info(**data):
        print("Packed Dictionary via **kwargs:", data)
    info(name="Sabeeha", age=19, sec="B")

    # Dynamic default instantiation via evaluations
    avg = lambda x, y, z: (x + y + z) / 3
    def square(a=avg(3, 4, 5)):
        return a * a
    print("Calculated square result value output:", square())
    print("-" * 40 + "\n")


# =========================================================================
# 13. RECTIFYING THE ITERATIVE MUTATION TRACKING ERROR
# =========================================================================
def demonstrate_list_mutations_trap():
    print("--- 13. Dynamic List Mutations Logic Wrap ---")
    List = [1, 2, 3, 4]
    print("Initial target tracking vector array list:", List)
    
    # CORRECTION NOTE: When removing elements inside a standard loop, 
    # indices shift dynamically causing elements to be skipped. 
    # Slice notation copy syntax (List[:]) is used to loop safely.
    for i in List[:]:
        if i == 2 or i == 3:
            List.remove(i)
    print("Safe modified array output result layout:", List)
    print("-" * 40 + "\n")


# =========================================================================
# 14. DATA WRAPPERS & CONSOLE UTILITIES
# =========================================================================
def demonstrate_palindromes_and_scopes():
    print("--- 14. Palindromes & Scopes ---")
    try:
        a = int(input("Enter an integer to check for palindrome alignment: "))
        b = 0
        temp = a
        while temp > 0:
            r = temp % 10
            b = (b * 10) + r
            temp = temp // 10
        if b == a:
            print("Result: You entered a palindrome entry.")
        else:
            print("Result: This number is not a palindrome.")
    except ValueError:
        print("Invalid numerical format parsed.")

    # Loop scope variable safety demo
    for i in range(5):
        pass
    print("Final leakage counter tracking value of loop outer boundary state 'i':", i)

    def greet():
        print("Hi from inner greeting block functional routine!")
    greet()
    print("-" * 40 + "\n")


# =========================================================================
# CENTRAL MASTER EXECUTION DRIVER
# =========================================================================
if __name__ == "__main__":
    demonstrate_geometry_and_math()
    demonstrate_conditionals_and_vowels()
    demonasing = demonstrate_aliasing_and_security()
    demonstrate_patterns_and_ascii()
    demonstrate_character_analytics()
    generate_password_utility()
    demonstrate_primes_and_combinatorics()
    demonstrate_binary_and_sets()
    demonstrate_matrix_and_comprehensions()
    calculate_gpa()
    demonstrate_recursion_fibonacci()
    demonstrate_lambda_and_args()
    demonstrate_list_mutations_trap()
    demonstrate_palindromes_and_scopes()
    
    print("All python architecture configuration scripts executed cleanly!")
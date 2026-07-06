# =========================================================================
# 1. NESTED DICTIONARIES & DATA TYPES
# =========================================================================
def demonstrate_nested_dictionaries():
    print("--- 1. Nested Dictionaries ---")
    a = {
        "name": "FATIMA",
        "Father name": "HUSSAIN ALI",
        "marks": "students",
        "Subjects": { 
            "English": 36,
            "Maths": 48,
            "Urdu": 56
        }    
    }
    print("Dictionary 'a':", a)
    print("Type of 'a':", type(a))
    print("-" * 40 + "\n")


# =========================================================================
# 2. DICTIONARY METHODS (ITEMS, GET, UPDATE)
# =========================================================================
def demonstrate_dictionary_methods():
    print("--- 2. Dictionary Methods (items, get, update) ---")
    a = {
        "Name": "Sabeeha Hussain",
        "Father name": "Hussain Ali",
        "Reg. no": "269"
    }
    print("Items (Pairs):", a.items())
    print("Get 'Name':", a.get("Name")) 
    
    # Adding a new key-value pair via update
    a.update({"City": "x,y,z"})
    print("After Update:", a)
    print("-" * 40 + "\n")


# =========================================================================
# 3. COMPREHENSIVE DICTIONARY USER INPUT
# =========================================================================
def demonstrate_dictionary_input():
    print("--- 3. Dynamic Dictionary From User Input ---")
    print("Example format: name:Ali, age:20, city:Lahore")
    user_input = input("Enter dict items (key:value) separated by commas: ")
    
    d = {}
    try:
        for item in user_input.split(","):
            if ":" in item:
                key, value = item.split(":")
                d[key.strip()] = value.strip()
        print("Generated Dictionary:", d)
    except Exception as e:
        print(f"Error processing layout configuration: {e}. Please use 'key:value' layout rules.")
    print("-" * 40 + "\n")


# =========================================================================
# 4. SAFE SEARCH LOOKUPS & DICTIONARY ITERATION
# =========================================================================
def demonstrate_lookups_and_loops():
    print("--- 4. Safe Lookups & Key-Value Iteration ---")
    dic = {'name': 'sabeeha', 'age': 19, 'father name': 'hussain ali'}
    print("Target Dictionary:", dic)
    
    # Square bracket vs .get() safety comparison
    print("Direct key read dic['name']:", dic['name'])     # Throws KeyError if missing
    print("Safe read dic.get('name'):", dic.get('name'))   # Safely returns None if missing
    
    # Fixed Loop Ordering: .items() always yields pairs as (key, value)
    for key, value in dic.items():     
        print(f"The value corresponding to the key [{key}] : {value}")
    print("-" * 40 + "\n")


# =========================================================================
# CENTRAL MASTER EXECUTION DRIVER
# =========================================================================
if __name__ == "__main__":
    demonstrate_nested_dictionaries()
    demonstrate_dictionary_methods()
    demonstrate_dictionary_input()  # Prompts for key-value pair string inputs
    demonstrate_lookups_and_loops()
    
    print("All python dictionary operations completed smoothly!")
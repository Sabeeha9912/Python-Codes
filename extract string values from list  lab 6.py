# extract string values from list
def extract_strings(data, index=0, result=None):
    if result is None:
        result = []
    if index == len(data):
        return result
    if isinstance(data[index], str):    # Check if the current element is a string
        result.append(data[index])
    return extract_strings(data, index + 1, result)  # call for next index
mixed_list = ["hello", 42, [1, 2], ("a", "b"), {"x", "y"}, "cyber", 100, "world"]
only_strings = extract_strings(mixed_list)
print("Original list:", mixed_list)
print("List with only strings:", only_strings)

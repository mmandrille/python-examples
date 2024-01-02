def compare_dicts(dict1, dict2, path=""):
    diff = {}
    
    for key in set(dict1.keys()) | set(dict2.keys()):
        new_path = f"{path}.{key}" if path else key

        if key not in dict1:
            diff[new_path] = {'added': dict2[key]}
        elif key not in dict2:
            diff[new_path] = {'removed': dict1[key]}
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            nested_diff = compare_dicts(dict1[key], dict2[key], path=new_path)
            if nested_diff:
                diff.update(nested_diff)
        elif dict1[key] != dict2[key]:
            diff[new_path] = {'old': dict1[key], 'new': dict2[key]}

    return diff

# Run our code
if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}
    dict2 = {'a': 1, 'b': 3, 'c': {'d': 3, 'f': 5, 'g': {'h': 6}}}

    # Same dict:
    print("Comparing same dict:")
    differences = compare_dicts(dict1, dict1)
    print(f"Differences: {differences}")

    print("\nComparing same dict1 & dict2:")
    differences = compare_dicts(dict1, dict2)
    print(f"Differences: {differences}")

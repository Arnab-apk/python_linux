def find_max_min(lst):
    max_val = max(lst)
    min_val = min(lst)
    max_idx = lst.index(max_val)
    min_idx = lst.index(min_val)
    
    return {
        'max': max_val,
        'max_index': max_idx,
        'min': min_val,
        'min_index': min_idx
    }

numbers = [3, 7, 2, 9, 1, 5]
result = find_max_min(numbers)
print(f"List: {numbers}")
print(f"Max: {result['max']} at index {result['max_index']}")
print(f"Min: {result['min']} at index {result['min_index']}")

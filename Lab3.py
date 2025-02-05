def find_large(arr):
    if not arr:
        return None
    
    max = arr[0]
    for i in arr[1:]:
        if i > max:
            max = i
    return max
print(find_large([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
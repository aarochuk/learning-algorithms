def binary_search(arr: list, item: int)->int:
    l = 0
    h = len(arr)-1
    while l <= h:
        m = int(l + (h-l)/2)
        if arr[m] == item:
            return m
        elif arr[m] > item:
            h = m-1
        else:
            l = m+1
    return -1

print(binary_search([1,2], 2))
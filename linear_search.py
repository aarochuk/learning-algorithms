def linear_search(haystack: list, num: int) -> bool:
    hay_len = len(haystack)
    for i in range(0, hay_len):
        if haystack[i] == num:
            return True
    return False

print(linear_search(['a', 'b', 'd', 'e'], 'e'))
def is_palindrome(data):
    # accepts both numerical and string data as input
    # convert input to lowercase string either way
    s = str(data).lower()

    if not s:
        return True  # Empty string is a palindrome

    left, right = 0, len(s) - 1

    # check if the first and last character are equivalent before looping
    if s[left] != s[right]:
        return False

    # while equivalent, move the pointers to check the next 2 positions
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# Test cases
assert is_palindrome("radar") == True
assert is_palindrome("RaDaR") == True
assert is_palindrome("hello") == False
assert is_palindrome("a") == True
assert is_palindrome(121) == True
assert is_palindrome(12345) == False
assert is_palindrome(12321) == True
assert is_palindrome("1A2B3B2A1") == True
assert is_palindrome("") == True

print("All tests passed successfully")

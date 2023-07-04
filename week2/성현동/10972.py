#10972
def is_palindrome(word):
    left, right = 0, len(word) - 1
    warn = 0
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        elif word[left + 1] == word[right]:
            warn += 1
            left += 1
        elif word[left] == word[right - 1]:
            warn += 1
            right -= 1
        else:
            return 2
        if warn > 1:
            return 2

    if warn == 1:
        return 1
    else:
        return 0


rep = int(input())
for _ in range(rep):
    result = is_palindrome(input())
    print(result)

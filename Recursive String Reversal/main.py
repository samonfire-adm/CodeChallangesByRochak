def reverse_string(s, left=0, right=None):
    if right is None:
        right = len(s) - 1
    if left >= right:
        return s
    s = list(s)
    s[left], s[right] = s[right], s[left]
    return reverse_string("".join(s), left + 1, right - 1)
    
print(reverse_string("Rochak Education"))
